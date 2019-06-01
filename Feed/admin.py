from django.contrib import admin
from .models import *


# Register your models here.
class SourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo')
    list_display_links = list_display


class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'venue', 'date', 'description', 'registration_link')
    list_display_links = list_display


class TutorialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published_date', 'link', 'source')
    list_display_links = list_display


class CommunitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'description', 'irc_link', 'community_link')
    list_display_links = list_display


admin.site.register(Source, SourceAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Communities, CommunitiesAdmin)
