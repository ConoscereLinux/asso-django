from django.views import generic

from academy.models import Event

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
    context_object_name = "courses"

    def get_queryset(self):
        """Return the last five published questions."""
        return Event.objects.order_by("-creation_date")[:10]
