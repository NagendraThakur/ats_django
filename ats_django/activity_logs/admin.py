from django.contrib import admin
from .models import ActivityLog

class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'target_type', 'target_id', 'created_at')
    search_fields = ('user__username', 'action')
    list_filter = ('target_type', 'created_at')

admin.site.register(ActivityLog, ActivityLogAdmin)
