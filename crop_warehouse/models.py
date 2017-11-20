# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Crop(models.Model):
	crop_name=models.CharField(max_length=30)
	catagory=models.CharField(max_length=30,help_text='Kharif or Rabi')
	crop_price_cur=models.IntegerField()
	crop_price_prev_kharif=models.IntegerField(help_text='1 year ago per kg Kharif',default=100)
	crop_price_prev_rabi=models.IntegerField(help_text='1 year ago per kg rabi',default=100)
	crop_price_prev1_kharif1=models.IntegerField(help_text='2 year ago per kg Kharif',default=100)
	crop_price_prev2_rabi1=models.IntegerField(help_text='2 year ago per kg rabi',default=100)
	
	def __unicode__(self):
		return self.crop_name

class Warehouse(models.Model):
	warehouse_name=models.CharField(max_length=30)
	location=models.CharField(max_length=30)
	capacity=models.IntegerField(default=100)
	price=models.IntegerField(help_text='monthly price',default=100)
	pincode=models.IntegerField(default=751020)
	def __unicode__(self):
		return self.warehouse_name
