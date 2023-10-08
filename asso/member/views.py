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


class MembershipTable(LoginRequiredMixin, generic.ListView):
    model = models.Membership
    template_name = "member/membership_table.html"
    context_object_name = "memberships"

    def get_queryset(self):
        query = super().get_queryset()
        if period := self.request.GET.get("period"):
            return query.filter(period__card_prefix=period)
        return query
