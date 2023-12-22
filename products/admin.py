from django.contrib import admin
from .models import Products, Chefs, PageAbout, Category

@admin.register(Products)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status', 'price']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

@admin.register(Category)
class ProductCategory(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Chefs)
class ChefList(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'position']
    list_filter = ['fname', 'lname', 'position']

@admin.register(PageAbout)
class AboutPage(admin.ModelAdmin):
    list_display = ['year', 'desc']
    list_filter = ['year']
    search_fields = ['year', 'desc']