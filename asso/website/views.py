import datetime as dt

from django.utils.translation import gettext_lazy as _
from django.views import generic

from asso.academy.models import Event

from .models import NavbarItem, SocialLink, ThemeConfig


def add_header_info_and_menu_items_to_context(request):
    """Context Processor for adding menu items and brand info

    See https://docs.djangoproject.com/en/4.2/ref/templates/api/#writing-your-own-context-processors
    """
    return {
        "menu_items": NavbarItem.objects.filter(active=True),
        "socials": SocialLink.objects.all(),
        "theme": ThemeConfig.objects.filter(active=True).first(),
    }


class HomePage(generic.TemplateView):
    template_name = "website/index.html"

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
                query = Event.objects.filter(start_date__gt=today)
                mode = "next"

        context["mode"] = mode
        context["courses"] = query.order_by("-start_date")[:10]

        return context
