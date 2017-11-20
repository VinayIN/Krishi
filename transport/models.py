# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.signals import post_save
# Create your models here.
class Transportation(models.Model):
	transport_company_name=models.CharField(max_length=30)
	location=models.CharField(max_length=30)
	capacity_per_person=models.IntegerField(help_text='per person capacity',default=100)
	trip_price_per_km=models.IntegerField(help_text='per km',default=100)
	pincode=models.IntegerField(default=751020)
	def __unicode__(self):
		return self.transport_company_name
	