import datetime as dt

from django.utils.translation import gettext_lazy as _
from django.views import generic

from .models import Event


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
                query = Event.objects.filter(end_date__lte=today)
            case "ongoing":
                query = Event.objects.filter(start_date__lte=today, end_date__gte=today)
            case "next" | _:
                query = Event.objects.filter(start_date__gte=today)
                mode = "next"

        context["event_query"] = mode
        context["event_queries"] = self.EVENT_QUERIES
        context["events"] = query.order_by("-start_date")[:10]
        return context


class EventList(EventListMixin, generic.ListView):
    model = Event
    template_name = "academy/events.html"
    context_object_name = "events"


class EventDetail(generic.DetailView):
    model = Event
    template_name = "academy/event.html"
    context_object_name = "event"


class EventCreate(generic.CreateView):
    model = Event
    fields = ["title", "subtitle"]


class EventUpdate(generic.UpdateView):
    model = Event
    fields = ["slug", "title", "subtitle"]
