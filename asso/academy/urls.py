from django.urls import path

from . import views

urlpatterns = [
    path("<slug:slug>/", views.EventDetailView.as_view(), name="event"),
]
