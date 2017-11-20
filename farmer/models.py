# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
import sys
sys.path.append("../")
from market.models import Market,market_crop_price
from transport.models import Transportation
from crop_warehouse.models import Crop,Warehouse


# Create your models here.




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=500, null=False,default="enter")
    pin = models.IntegerField(null=False,default=000000)
    aadhar = models.IntegerField(null=False,default=111222)
    crops=models.ManyToManyField(Crop,null=True)
    warehouses=models.ManyToManyField(Warehouse,null=True)
    markets=models.ManyToManyField(Market,null=True)
    transportation=models.ManyToManyField(Transportation,null=True)

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()