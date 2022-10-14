from django import forms

from pascal.club_and_cell.models import ClubCell
from pascal.users.models import User


class ClubCellForm(forms.ModelForm):
    class Meta:
        model = ClubCell
        fields = ("name", "club_or_cell", "faculty_head", "members")

    def __init__(self, *args, **kwargs):
        super(ClubCellForm, self).__init__(*args, **kwargs)
        faculty_head_choices = [(fh.id, fh.username) for fh in User.objects.filter(user_choice="FH")]
        self.fields["faculty_head"] = forms.ChoiceField(choices=faculty_head_choices)
