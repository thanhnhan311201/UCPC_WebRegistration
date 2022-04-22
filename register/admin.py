from django.contrib import admin
from .models import School, Team
# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    search_fields = ['school1', 'school2', 'school3']

class TeamAdmin(admin.ModelAdmin):
    list_display = ('team', 'school1', 'school2', 'school3')
    list_filter = ['school1', 'school2', 'school3']
    search_fields = ['team']

admin.site.register(School, SchoolAdmin)
admin.site.register(Team, TeamAdmin)
