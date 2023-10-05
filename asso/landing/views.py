import datetime as dt

from django.utils.translation import gettext_lazy as _
from django.views import generic

from asso.academy.models import Event


class HomePage(generic.TemplateView):
    template_name = "home.html"

    MODES = {
        "next": _("Prossimi Eventi"),
        "current": _("In corso"),
        "archive": _("Archivio"),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["modes"] = self.MODES

        today = dt.date.today()

        match mode := self.request.GET.get("mode"):
            case "archive":
                query = Event.objects.filter(end_date__lt=today)
            case "current":
                query = Event.objects.filter(start_date__lt=today, end_date__gt=today)
            case "next" | _:
                query = Event.objects.filter(start_date__gte=today)
                mode = "next"

        context["mode"] = mode
        context["courses"] = query.order_by("-start_date")[:10]

        return context
