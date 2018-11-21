from django.contrib import admin
from .models import Store, MenuItem
# Register your models here.



# @admin.register(MenuItem)
# class MenuItemAdmin(admin.ModelAdmin):
#     list_display = ['name', 'price']

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'notes']
    inlines = [MenuItemInline]