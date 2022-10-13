from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django import forms
from django.contrib.auth import forms as admin_forms, password_validation
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from pascal.users.models import Department

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(forms.ModelForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = (
            "user_choice", "username", "first_name", "last_name", "department", "email", "phone", "sem", "password",
            "confirm_password",
        )

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        self.fields["password"].widget = forms.PasswordInput()

    def clean(self):
        cleaned_data = super(UserSignupForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        try:
            password_validation.validate_password(password, self.instance)
        except forms.ValidationError as error:
            self.add_error('password', error)

        if password != confirm_password:
            self.add_error('password', "Password and Confirm password does not match")
        return cleaned_data

    def save(self, commit=True):
        user = super(UserSignupForm, self).save(commit=True)
        user.set_password(user.password)
        user.save()
        return user


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ("name",)
