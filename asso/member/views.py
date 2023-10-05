from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from . import models


class MemberDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "member/member.html"
    context_object_name = "member"
    model = models.Member


class MemberCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Member
    fields = ["user", "cf", "sex", "phone"]
