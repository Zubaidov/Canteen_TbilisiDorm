from django.contrib import admin
from .models import Menu, Chefs

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status', 'price']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

@admin.register(Chefs)
class ChefList(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'position']
    list_filter = ['fname', 'lname', 'position']