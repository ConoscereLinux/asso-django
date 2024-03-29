import datetime as dt

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.views import generic

from . import forms, models


class EventListMixin(generic.base.ContextMixin, generic.View):
    EVENT_QUERIES = [
        ("next", _("Next events")),
        ("ongoing", _("Ongoing")),
        ("archive", _("Archive")),
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = dt.date.today()
        match mode := self.request.GET.get("mode"):
            case "archive":
                query = models.Event.objects.filter(end_date__lte=today)
            case "ongoing":
                query = models.Event.objects.filter(
                    start_date__lte=today, end_date__gte=today
                )
            case "next" | _:
                query = models.Event.objects.filter(start_date__gte=today)
                mode = "next"

        context["event_query"] = mode
        context["event_queries"] = self.EVENT_QUERIES
        context["events"] = query.order_by("-start_date")[:10]
        return context


class EventList(EventListMixin, generic.ListView):
    model = models.Event
    template_name = "academy/events.html"
    context_object_name = "events"


class EventDetail(generic.DetailView):
    model = models.Event
    template_name = "academy/event.html"
    context_object_name = "event"


class EventCreate(PermissionRequiredMixin, generic.CreateView):
    permission_required = "academy.add_event"
    model = models.Event
    fields = "__all__"


class EventUpdate(PermissionRequiredMixin, generic.UpdateView):
    permission_required = "academy.update_event"
    model = models.Event
    fields = "__all__"


class EventEnroll(generic.CreateView):
    template_name = "academy/event_enrollment.html"
    model = models.Enrollment
    form_class = forms.EnrollForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs["initial"]["event"] = get_object_or_404(
            models.Event, slug=self.kwargs["slug"]
        )
        if hasattr(self.request.user, "email"):
            kwargs["initial"]["email"] = self.request.user.email
        if hasattr(self.request.user, "member"):
            kwargs["initial"]["phone"] = self.request.user.member.phone

        return kwargs
