import datetime as dt

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


class EventCreate(generic.CreateView):
    model = models.Event
    fields = [
        "title",
        "subtitle",
        "category",
        "approval_state",
        "need_membership",
        "price",
        "trainers",
    ]


class EventEnroll(generic.CreateView):
    model = models.Enrollment
    fields = ["email", "phone"]


class EventUpdate(generic.UpdateView):
    model = models.Event
    fields = ["slug", *EventCreate.fields]
