from .models import NavbarItem, SocialLink, ThemeConfig


def add_header_and_footer_info(request):
    """Context Processor for adding menu items and brand info

    See https://docs.djangoproject.com/en/4.2/ref/templates/api/#writing-your-own-context-processors
    """
    return {
        "menu_items": NavbarItem.objects.filter(show=True),
        "socials": SocialLink.objects.filter(show=True).all(),
        "theme": ThemeConfig.objects.filter(active=True).first(),
    }
