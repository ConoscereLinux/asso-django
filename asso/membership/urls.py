from django.urls import path

from . import views

urlpatterns = [
    path("<int:pk>/", views.MemberDetailView.as_view(), name="member"),
]
