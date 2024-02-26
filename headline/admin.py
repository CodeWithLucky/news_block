from django.contrib import admin
from . models import NewsMod

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'author', 'date', 'content', 'image'
    ]

admin.site.register(NewsMod, NewsAdmin)
        