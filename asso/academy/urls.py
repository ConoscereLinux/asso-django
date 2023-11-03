from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.EventList.as_view(), name="events"),
    path("detail/<slug:slug>/", views.EventDetail.as_view(), name="event"),
    path("create/", views.EventCreate.as_view(), name="event-create"),
    path("update/<slug:slug>/", views.EventUpdate.as_view(), name="event-update"),
]
