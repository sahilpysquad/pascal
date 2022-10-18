from django.urls import path

from pascal.event.views import PlaceCreateView, EventCreateView, EventListView, EventDetailsCreateView

app_name = "events"
urlpatterns = [
    path("create-place/", PlaceCreateView.as_view(), name="create_place"),
    path("create-event-details/<int:pk>/", EventDetailsCreateView.as_view(), name="create_event_details"),
    path("create-event/", EventCreateView.as_view(), name="create_event"),
    path("event-list/", EventListView.as_view(), name="event_list"),
]
