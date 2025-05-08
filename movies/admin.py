from django.contrib import admin
from movies.models import Movies

@admin.register(Movies)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_date', 'resume')