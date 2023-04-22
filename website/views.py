from django.views import generic

from academy.models import Event


class IndexView(generic.ListView):
    template_name = "website/index.html"
    context_object_name = "courses"

    def get_queryset(self):
        """Return the last five published questions."""
        return Event.objects.order_by("creation_date")[:5]
