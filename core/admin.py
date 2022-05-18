from django.contrib import admin
from .models import AboutMeModel

# Register your models here.
@admin.register(AboutMeModel)

class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('created', 'modified', 'active')