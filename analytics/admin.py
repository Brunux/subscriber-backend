# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Planning, Record, Tender, Publisher, Buyer, Tag, Contracts, Parties, Awards


# Register your models here.

@admin.register(Planning)
class EventAdmin(admin.ModelAdmin):
    list_display = ('budget_classification_level_label', 'budget_classification_level_description', 'budget_classification_level_label',)

@admin.register(Record)
class EventAdmin(admin.ModelAdmin):
    list_display = ('ocid', 'planning',)


@admin.register(Tender)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'description', 'amount', 'period',)

@admin.register(Publisher)
class EventAdmin(admin.ModelAdmin):
    list_display = ('uri', 'uid', 'name',)

@admin.register(Buyer)
class EventAdmin(admin.ModelAdmin):
    list_display = ('buyerName', 'buyerId',)

@admin.register(Contracts)
class EventAdmin(admin.ModelAdmin):
    list_display = ('contract_title', 'status', 'contract_details', 'amount', 'period',)

@admin.register(Parties)
class EventAdmin(admin.ModelAdmin):
    list_display = ('partie_id', 'partie_name', 'contact_name', 'contact_name', 'contact_email',)

@admin.register(Awards)
class EventAdmin(admin.ModelAdmin):
    list_display = ('award_title', 'award_description', 'award_id',)


@admin.register(Tag)
class EventAdmin(admin.ModelAdmin):
    list_display = ('cero',)



