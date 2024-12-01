from django.contrib import admin
from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job', 'status', 'applied_at')
    search_fields = ('candidate__name', 'job__title')
    list_filter = ('status', 'job__title')

admin.site.register(Application, ApplicationAdmin)
