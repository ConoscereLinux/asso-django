from django.urls import path

from . import views

urlpatterns = [
    path("detail/<int:pk>/", views.MemberDetailView.as_view(), name="member"),
]
