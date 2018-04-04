# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Tender(models.Model):
    title = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    procurentMethodRationale = models.CharField(max_length=30)
    procurentMethod = models.CharField(max_length=30)
    tenderId = models.CharField(max_length=10)
    hasEnquiries = models.BooleanField()
    description = models.CharField(max_length=100)

    amount = models.IntegerField()
    period = models.DateTimeField()
    submissionMethod = models.CharField(max_length=10)
    procuringEntityName =  models.CharField(max_length=30)
    procuringEntityId = models.CharField(max_length=30)
    enquiryPeriodStartDate = models.DateTimeField()


class Publiser(models.Model):
	uri = models.URLField()
	uid = models.CharField(max_length=10)
	name = models.CharField(max_length=30)


class Buyer(models.Model):
    oic = models.CharField(max_length=30)
    language = models.CharField(max_length=30)
    initiationType = models.CharField(max_length=30)
    buyerId = models.CharField(max_length=10)
    buyerName = models.CharField(max_length=30	)
    date =  models.DateTimeField()



class Tag(models.Model):					
    cero = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.cero)



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

