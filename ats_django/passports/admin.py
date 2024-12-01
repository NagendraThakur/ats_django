from django.contrib import admin
from .models import Passport

class PassportAdmin(admin.ModelAdmin):
    list_display = ('passport_number','first_name', 'last_name')
    search_fields = ('passport_number','first_name', 'last_name')

admin.site.register(Passport, PassportAdmin)