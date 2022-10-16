from django import forms

from pascal.club_and_cell.models import ClubCell
from pascal.users.models import User


class ClubCellForm(forms.ModelForm):
    class Meta:
        model = ClubCell
        fields = ("name", "club_or_cell", "faculty_head", "members")

    def __init__(self, *args, **kwargs):
        super(ClubCellForm, self).__init__(*args, **kwargs)
        self.fields["faculty_head"] = forms.ModelChoiceField(User.objects.filter(user_choice="FH", is_active=True))
        self.fields["members"] = forms.ModelMultipleChoiceField(User.objects.filter(
            user_choice__in=["FM", "ST"], is_active=True)
        )
