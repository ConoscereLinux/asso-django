from django.views import generic

from . import models


class EventList(generic.ListView):
    model = models.Event
    template_name = "academy/events.html"
    context_object_name = "events"


class EventDetailView(generic.DetailView):
    model = models.Event
    template_name = "academy/event.html"
    context_object_name = "event"
