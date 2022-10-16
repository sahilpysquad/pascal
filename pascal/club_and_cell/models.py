from django.db import models
from django.utils.translation import gettext_lazy as _

from pascal.users.models import User


class ClubCell(models.Model):
    CLUB_OR_CELL = (
        ("CB", "Club"),
        ("CL", "Cell")
    )

    name = models.CharField(verbose_name=_("Name"), max_length=200)
    club_or_cell = models.CharField(verbose_name=_("Club or Cell"), max_length=2, choices=CLUB_OR_CELL, default="CB")
    faculty_head = models.ForeignKey(
        verbose_name=_("Faculty Head"), to=User, on_delete=models.CASCADE, related_name="faculty_head"
    )
    members = models.ManyToManyField(verbose_name=_("Members"), to=User, related_name="members")
    created_at = models.DateTimeField(verbose_name=_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Updated At"), auto_now=True)
    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True)

    def __str__(self):
        return self.name

    def get_basic_info(self):
        data = {
            "name": self.name,
            "club_or_cell": dict(self.CLUB_OR_CELL).get(self.club_or_cell)
        }
        return data

    def club_or_cell_verbose(self):
        return dict(ClubCell.CLUB_OR_CELL)[self.club_or_cell]
