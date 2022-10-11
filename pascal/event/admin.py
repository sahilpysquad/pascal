from django.contrib import admin

from pascal.event.models import Place, Event, EventDetails


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "is_organised")


@admin.register(EventDetails)
class EventDetailsAdmin(admin.ModelAdmin):
    list_display = ("id", )
