from django.views import generic

from . import models


class MemberDetailView(generic.DetailView):
    template_name = "membership/member.html"
    context_object_name = "member"
    model = models.Member
