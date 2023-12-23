from django.contrib import admin
from .models import Products, Chefs, PageAbout, Category

@admin.register(Products)
class Products(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'amount', 'category', 'created', 'updated']
    list_filter = ['status', 'created', 'publish', 'author']
    list_editable = ['price', 'amount']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

@admin.register(Category)
class ProductCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Chefs)
class ChefList(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'position']
    list_filter = ['fname', 'lname', 'position']

@admin.register(PageAbout)
class AboutPage(admin.ModelAdmin):
    list_display = ['year', 'desc']
    list_filter = ['year']
    search_fields = ['year', 'desc']