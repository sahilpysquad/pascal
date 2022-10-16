from django.contrib.postgres.fields import ArrayField
from django.db import models

from pascal.club_and_cell.models import ClubCell
from pascal.users.models import User


class Place(models.Model):
    name = models.CharField(verbose_name="Name", max_length=200)
    address = models.TextField(verbose_name="Address")

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(verbose_name="Name", max_length=200)
    club_cell = models.ManyToManyField(verbose_name="Clubs and Cells", to=ClubCell, related_name="clubs_cells")
    invited_faculty = models.ManyToManyField(
        verbose_name="Invited Faculties", to=User, related_name="invited_faculties"
    )
    start_at = models.DateTimeField(verbose_name="Start On")
    end_at = models.DateTimeField(verbose_name="End On")
    place = models.ForeignKey(verbose_name="Place", to=Place, on_delete=models.DO_NOTHING)
    is_organised = models.BooleanField(verbose_name="Is Organised", default=False)

    def __str__(self):
        return self.name

    def date_verbose(self):
        return dict(ClubCell.CLUB_OR_CELL)[self.club_or_cell]


class EventDetails(models.Model):
    event = models.OneToOneField(verbose_name="Event", to=Event, on_delete=models.CASCADE, related_name="event")
    summary = models.TextField(verbose_name="Summary", null=True, blank=True)
    report_file = models.CharField(verbose_name="Report File", max_length=2000, null=True, blank=True)
    images = ArrayField(verbose_name="Images", base_field=models.CharField(max_length=2000), null=True, blank=True)
    rating = models.JSONField(verbose_name="Rating", null=True, blank=True)

    def __str__(self):
        return self.event.name
