from django.contrib import admin

from pascal.club_and_cell.models import ClubCell


@admin.register(ClubCell)
class ClubCellAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
