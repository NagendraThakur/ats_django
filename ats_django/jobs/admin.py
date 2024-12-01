from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'location', 'created_by', 'created_at')
    search_fields = ('title',)
    list_filter = ('status', 'location')

admin.site.register(Job, JobAdmin)
