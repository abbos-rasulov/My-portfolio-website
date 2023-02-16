from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
from django.db import models


@admin.register(JobSkill)
class JobSkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']
    search_fields = ['name']
    date_hierarchy = 'created'
    list_filter = ['created', 'updated']


@admin.register(SoftSkill)
class SoftSkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']
    search_fields = ['name']
    date_hierarchy = 'created'
    list_filter = ['created', 'updated']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated', 'available']
    search_fields = ['name', 'description']
    date_hierarchy = 'created'
    list_filter = ['created', 'updated', 'available']
    formfield_overrides = {
        models.TextField: {
            'widget': TinyMCE()
        }
    }


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created', 'updated']
    search_fields = ['name', 'description']
    date_hierarchy = 'created'
    list_filter = ['created', 'updated']
    formfield_overrides = {
        models.TextField: {
            'widget': TinyMCE()
        }
    }


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created', 'updated']
    search_fields = ['name', 'description']
    date_hierarchy = 'created'
    list_filter = ['created', 'updated']
    formfield_overrides = {
        models.TextField: {
            'widget': TinyMCE()
        }
    }


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'job', 'image', 'created', 'updated']
    search_fields = ['name', 'description']
    date_hierarchy = 'created'
    list_filter = ['created', 'updated']
    formfield_overrides = {
        models.TextField: {
            'widget': TinyMCE()
        }
    }


@admin.register(UserContact)
class UserContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created', 'updated']
    search_fields = ['name', 'message']
    date_hierarchy = 'created'
    list_filter = ['created', 'updated']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    date_hierarchy = 'created'
    list_filter = ['created', 'updated']


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'image', 'created', 'updated']
    search_fields = ['name', 'description']
    date_hierarchy = 'created'
    list_filter = ['created', 'updated']
    formfield_overrides = {
        models.TextField: {
            'widget': TinyMCE()
        }
    }