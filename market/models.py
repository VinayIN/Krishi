
from django.db import models
import sys
sys.path.append("../")
from crop_warehouse.models import Crop, Warehouse

class Market(models.Model):
	market_name=models.CharField(max_length=30)
	location=models.CharField(max_length=30)
	capacity=models.IntegerField(default=100)
	pincode=models.IntegerField(default=751020)
	def __unicode__(self):
		return self.market_name


class market_crop_price(models.Model):
	market_id=models.ForeignKey(Market,on_delete=models.CASCADE)
	crop_id=models.ForeignKey(Crop,on_delete=models.CASCADE)
	price_per_kg=models.IntegerField(default=100)
	crop_price_prev_kharif=models.IntegerField(help_text='1 year ago per kg Kharif',default=100)
	crop_price_prev_rabi=models.IntegerField(help_text='1 year ago per kg rabi',default=100)
	crop_price_prev1_kharif=models.IntegerField(help_text='2 year ago per kg Kharif',default=100)
	crop_price_prev2_rabi=models.IntegerField(help_text='2 year ago per kg rabi',default=100)
	

	def __unicode__(self):
		return (self.market_id.market_name)