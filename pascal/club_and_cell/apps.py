from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _


class ClubAndCellConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pascal.club_and_cell'
    verbose_name = _("Clubs and Cells")
