from django.views import generic

from . import models


class MemberDetailView(generic.DetailView):
    template_name = "member/member.html"
    context_object_name = "member"
    model = models.Member


class MemberCreateView(generic.CreateView):
    model = models.Member
    fields = ["user", "cf", "sex", "phone"]
