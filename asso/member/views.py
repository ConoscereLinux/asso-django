from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from . import models


class MemberDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Member
    template_name = "member/member.html"
    context_object_name = "member"


class MemberCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Member
    fields = ["user", "first_name", "last_name", "cf", "gender", "phone"]
