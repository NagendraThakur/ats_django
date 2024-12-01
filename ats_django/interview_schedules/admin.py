from django.contrib import admin
from .models import InterviewSchedule

class InterviewScheduleAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job', 'scheduled_by', 'date_time', 'mode')
    search_fields = ('candidate__name', 'job__title')
    list_filter = ('mode', 'date_time')

admin.site.register(InterviewSchedule, InterviewScheduleAdmin)
