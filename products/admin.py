from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ("barcode", "title", "amount", "price", "created_at")

admin.site.register(Menu, MenuAdmin)