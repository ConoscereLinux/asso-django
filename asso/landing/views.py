from django.views import generic

from asso.academy.views import EventListMixin


class HomePage(generic.TemplateView, EventListMixin):
    template_name = "landing/home.html"
