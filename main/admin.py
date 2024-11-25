from django.contrib import admin
from main.models import Navigate
# Register your models here.

@admin.register(Navigate)
class NavigateAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}