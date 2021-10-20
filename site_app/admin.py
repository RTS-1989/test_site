from django.contrib import admin

from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'update_date']
    ordering = ['title']
    search_fields = ['title']
