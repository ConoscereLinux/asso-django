from django.views import generic

from . import models


class EventDetailView(generic.DetailView):
    model = models.Event
    template_name = "academy/event.html"
    context_object_name = "event"
