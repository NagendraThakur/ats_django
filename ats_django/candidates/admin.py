from django.contrib import admin
from applications.models import Application
from interview_schedules.models import InterviewSchedule
from notes.models import Note
from passports.models import Passport
from .models import Candidate

# Inline for Applications to be displayed inside Candidate's admin form
class ApplicationInline(admin.TabularInline):
    model = Application
    extra = 1  # Number of empty forms to display when editing Candidate

# Inline for Interview Schedules
class InterviewScheduleInline(admin.TabularInline):
    model = InterviewSchedule
    extra = 0

# Inline for Notes
class NoteInline(admin.TabularInline):
    model = Note
    extra = 1

# Inline for Passports
class PassportInline(admin.TabularInline):
    model = Passport
    extra = 1
    can_delete = False  # Disable the option to delete passports from the inline form


# Custom admin for Candidate
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'created_at', 'updated_at')
    search_fields = ('name', 'email')
    list_filter = ('status',)
    inlines = [ApplicationInline, InterviewScheduleInline, NoteInline, PassportInline]



admin.site.register(Candidate, CandidateAdmin)
