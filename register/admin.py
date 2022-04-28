from django.contrib import admin
from .models import Team
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ('team', 'school1', 'school2', 'school3')
    list_filter = ['school1', 'school2', 'school3']
    search_fields = ['team']

admin.site.register(Team, TeamAdmin)
