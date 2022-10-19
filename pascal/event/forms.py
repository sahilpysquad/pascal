from django import forms
from django.contrib.admin import widgets

from pascal.event.models import Event, Place, EventDetails
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


class EventDetailsForm(forms.ModelForm):
    class Meta:
        model = EventDetails
        fields = ("event", "report_file", "images", "summary")
        widgets = {
            "report_file": forms.widgets.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super(EventDetailsForm, self).__init__(*args, **kwargs)
        self.fields["images"] = forms.ImageField(
            required=False,
            widget=forms.ClearableFileInput(attrs={'multiple': True})
        )
