# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Record(models.Model):
    """
    Main data structure
    """
    ocid = models.CharField('OCID', max_length=50)
    planning = models.ForeignKey('Planning')

    def __str__(self):
        return '{}'.format(self.ocid)


class Planning(models.Model):
    """
    First stage of the open contratcs standar please check documentation at: url-here
    """

    budget_break_down_url = models.URLField()
    budget_break_down_description = models.CharField('Budget Description', max_length=50)
    budget_break_down_id = models.IntegerField()
    budget_classification_level_label = models.CharField('Level Label', max_length=50)
    budget_classification_level_description = models.CharField('Level description',  max_length=50)

    def __str__(self):
        return '{}'.format(self.budget_classification_level_label)
