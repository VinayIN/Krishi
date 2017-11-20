# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Market)
admin.site.register(models.market_crop_price)
