# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Tender(models.Model):
    """
    Tender doc here
    """
    title = models.CharField(max_length=250)
    status = models.CharField(max_length=30)
    procurentMethodRationale = models.CharField(max_length=30)
    procurentMethod = models.CharField(max_length=30)
    tenderId = models.CharField(max_length=10)
    hasEnquiries = models.BooleanField()
    description = models.CharField(max_length=250)

    amount = models.IntegerField()
    period = models.DateTimeField()
    submissionMethod = models.CharField(max_length=10)
    procuringEntityName =  models.CharField(max_length=30)
    procuringEntityId = models.CharField(max_length=30)
    enquiryPeriodStartDate = models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.title)


class Publisher(models.Model):
    """
    Publisher doc here
    """
    uri = models.URLField()
    uid = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.name)


class Buyer(models.Model):
    """
    Buyer doc here
    """
    oic = models.CharField(max_length=100)
    language = models.CharField(max_length=30)
    initiationType = models.CharField(max_length=30)
    buyerId = models.CharField(max_length=10)
    buyerName = models.CharField(max_length=250)
    date =  models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.buyerName)


class Tag(models.Model):
    """
    Tag doc here
    """
    cero = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.cero)


class Record(models.Model):
    """
    Main data structure
    """
    ocid = models.CharField('OCID', max_length=50)
    planning = models.ForeignKey('Planning')
    tender = models.ForeignKey('Tender')
    publisher = models.ForeignKey('Publisher')
    buyer = models.ForeignKey('Buyer')
    tag = models.ForeignKey('Tag')
    contratcs = models.ForeignKey('Contracts')
    parties = models.ForeignKey('Parties')
    awards = models.ForeignKey('Awards')


    def __str__(self):
        return '{}'.format(self.ocid)


class Planning(models.Model):
    """
    First stage of the open Planning standar please check documentation at: url-here
    """

    budget_break_down_url = models.URLField()
    budget_break_down_description = models.CharField('Budget Description', max_length=250)
    budget_break_down_id = models.IntegerField()
    budget_classification_level_label = models.CharField('Level Label', max_length=250)
    budget_classification_level_description = models.CharField('Level description',  max_length=50)

    def __str__(self):
        return '{}'.format(self.budget_classification_level_label)


class Contracts(models.Model):
    """
    First stage of the open contratcs standar please check documentation at: url-here
    """

    value_with_tax = models.CharField(max_length=50)

    contract_title = models.CharField(max_length=250)
    implementation = models.CharField(max_length=250)
    suppliers = models.CharField(max_length=50)
    buyers = models.CharField(max_length=50)
    date_signed = models.CharField(max_length=50)
    period = models.CharField(max_length=50)
    award_id = models.CharField(max_length=50)
    contract_id = models.IntegerField()
    amount = models.IntegerField()
    status = models.CharField(max_length=50)
    contract_details = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.contract_id, self.contract_title, self.status, self.contract_details)


class Parties(models.Model):
    """
    First stage of the open parties standar please check documentation at: url-here
    """

    contact_telephone = models.CharField(max_length=50)
    contact_email   = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50)
    street_adress =  models.CharField(max_length=250)
    region = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    country_name = models.CharField(max_length=50)
    partie_name = models.CharField(max_length=250)
    partie_id = models.CharField(max_length=50)
    
    def __str__(self):
        return '{}'.format(self.partie_id, self.partie_name, self.contact_name, self.contact_email)


class Awards(models.Model):
    """
    First stage of the open Awards standar please check documentation at: url-here
    """

    award_title = models.CharField('Awards title', max_length=250)
    award_description = models.CharField('Awards description', max_length=250)
    award_id = models.CharField('Awards id', max_length=50)
    currency =  models.CharField('currency', max_length=15)
    amount = models.IntegerField()
    supplier_name = models.CharField('Supplier name',max_length=250)
    supplier_id = models.CharField('Supplier id',max_length=30)
    contract_start_date = models.DateTimeField()
    contract_end_date = models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.award_title, self.award_description, self.award_id, )
