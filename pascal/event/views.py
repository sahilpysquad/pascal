from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView
from django.utils.translation import gettext_lazy as _

from pascal.event.forms import PlaceForm, EventForm
from pascal.event.models import Place, Event


class PlaceCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Place
    form_class = PlaceForm
    template_name = "event/event_place_list.html"
    success_url = "/events/create-place"
    success_message = _("Place added successfully.")

    def get_context_data(self, **kwargs):
        response = super(PlaceCreateView, self).get_context_data(**kwargs)
        places = Place.objects.all()
        response["places"] = places
        return response


class EventListView(LoginRequiredMixin,ListView):
    model = Event
    template_name = "events/event_list.html"
    context_object_name = "events"
    queryset = Event.objects.all().order_by("id")


class EventCreateView(LoginRequiredMixin, SuccessMessageMixin,CreateView):
    model = Event
    form_class = EventForm
    template_name = "event/event_create_form.html"
    success_message = _("Event created successfully.")
    success_url = "/event/event-list"

