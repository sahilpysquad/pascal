from django import forms
from django.contrib.admin import widgets

from pascal.event.models import Event, Place
from pascal.users.models import User


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ("name", "address")


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ("name", "club_cell", "invited_faculty", "place", "start_at", "end_at")
        widgets = {
            'start_at': forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_at': forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'})
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields["invited_faculty"] = forms.ModelMultipleChoiceField(
            User.objects.filter(user_choice__in=["FH", "FH", "OT"])
        )
