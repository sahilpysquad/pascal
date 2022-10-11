from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from pascal.utils.helper_methods import get_normalize_date


class Department(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=100)

    def __str__(self):
        return self.name


class User(AbstractUser):
    """
    Default custom user model for pascal.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    USER_CHOICES = (
        ("FH", "Faculty Head"),
        ("FM", "Faculty Member"),
        ("ST", "Student"),
        ("OT", "Other")
    )

    STATUS = (
        ("RQ", "Requested"),
        ("AP", "Approved"),
        ("RJ", "Rejected"),
    )

    email = models.EmailField(verbose_name=_("Email"), unique=True)
    phone = models.CharField(
        verbose_name=_("Phone Number"),
        max_length=20, null=True, blank=True, unique=True,
        validators=[RegexValidator(r'^[6-9]\d{9}$')]
    )
    is_phone_verified = models.BooleanField(verbose_name=_("Is Phone Verified"), default=False)
    is_email_verified = models.BooleanField(verbose_name=_("Is Email Verified"), default=False)
    user_choice = models.CharField(verbose_name=_("User Choice"), max_length=2, default="ST", choices=USER_CHOICES)
    status = models.CharField(verbose_name=_("Status"), max_length=2, default="RQ", choices=STATUS)
    department = models.ForeignKey(
        verbose_name=_("Department"), to=Department, null=True, blank=True, on_delete=models.CASCADE
    )
    sem = models.PositiveSmallIntegerField(verbose_name=_("Semester"), null=True, blank=True)
    otp = models.PositiveIntegerField(verbose_name=_("OTP"), null=True, blank=True)
    email_token = models.CharField(verbose_name=_("Email Token"), max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username

    def get_basic_info(self):
        data = {
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": f"{self.first_name} {self.last_name}",
            "created_at": get_normalize_date(self.date_joined),
            "user_choice": dict(self.USER_CHOICES).get(self.user_choice),
            "status": dict(self.STATUS).get(self.status),
            "phone": self.phone,
            "is_phone_verified": self.is_phone_verified,
            "email": self.email,
            "is_email_verified": self.is_email_verified,
            "sem": self.sem,
            "department": self.department.name if self.department else None
        }
        return data

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
