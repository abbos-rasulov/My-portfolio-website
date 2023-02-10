from django.contrib import admin
from .models import Skill, Service, Education, Experience
from tinymce.widgets import TinyMCE
from django.db import models


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'updated', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    date_hierarchy = 'created'
    list_editable = ['available']
    list_filter = ['available', 'created', 'updated']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    date_hierarchy = 'created'
    list_filter = ['created', 'updated']
    formfield_overrides = {
        models.TextField: {
            'widget': TinyMCE()
        }
    }


@admin.register(Education)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created', 'updated']
    search_fields = ['name', 'description']
    date_hierarchy = 'created'
    list_filter = ['created', 'updated']


@admin.register(Experience)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created', 'updated']
    search_fields = ['name', 'description']
    date_hierarchy = 'created'
    list_filter = ['created', 'updated']
