from django.contrib import admin
from .models import *


# Register your models here.
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')
    list_display_links = list_display


class EventsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'time', 'link', 'source', 'image',)
    list_display_links = list_display


class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'registration_link', 'source')
    list_display_links = list_display


class CommunitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'description', 'irc_link', 'community_link')
    list_display_links = list_display


admin.register(Source, SourceAdmin)
admin.register(Events, EventsAdmin)
admin.register(Tutorial, TutorialAdmin)
admin.register(Communities, CommunitiesAdmin)
