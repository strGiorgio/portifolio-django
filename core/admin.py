from django.contrib import admin
from .models import AboutMeModel, IdiomsModel

# Register your models here.
@admin.register(AboutMeModel)
@admin.register(IdiomsModel)

class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('created', 'modified', 'active')

class IdiomsModelAdmin(admin.ModelAdmin):
    list_display = ('lang', 'level', 'created', 'modified')