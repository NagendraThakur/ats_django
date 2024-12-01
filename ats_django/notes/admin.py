from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'user', 'created_at', 'note')
    search_fields = ('candidate__name', 'user__username')
    list_filter = ('created_at',)

admin.site.register(Note, NoteAdmin)
