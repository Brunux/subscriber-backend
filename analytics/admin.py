# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Planning, Record

# Register your models here.

@admin.register(Planning)
class EventAdmin(admin.ModelAdmin):
    list_display = ('budget_classification_level_label', 'budget_classification_level_description', 'budget_classification_level_label',)

@admin.register(Record)
class EventAdmin(admin.ModelAdmin):
    list_display = ('ocid', 'planning',)
