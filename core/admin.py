from django.contrib import admin
from .models import AboutMeModel, KnowledgesModel, IdiomsModel, SkillsModel

# Register your models here.
@admin.register(AboutMeModel)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('created', 'modified', 'active')

@admin.register(IdiomsModel)
class IdiomsModelAdmin(admin.ModelAdmin):
    list_display = ('lang', 'level', 'created', 'modified')

@admin.register(SkillsModel)
class SkillsModelAdmin(admin.ModelAdmin):
    list_display = ('skill', 'percentage', 'created', 'modified', 'active')

@admin.register(KnowledgesModel)
class KnowledgesModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'modified', 'active')