from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from models import Market,market_crop_price

def processQuery(loc,crop,price,quant):
	if(len(loc[0])==0 and len(crop[0])==0 and len(price[0])==0 and len(quant[0])!=0):
		#data=Market.objects.filter(capacity>=quant)
		data=Market.objects.raw('select * from market_market where capacity >=%s',quant)
		return data
	if(len(loc[0])==0 and len(crop[0])==0 and len(price[0])!=0 and len(quant[0])==0):
		#data=market_crop_price.objects.filter(price_per_kg>=price)
		
		data=market_crop_price.objects.raw('select * from market_market_crop_price,market_market where market_market_crop_price.market_id_id =market_market.id and price_per_kg >=%s',price)
		return data
	if(len(loc[0])==0 and len(crop[0])==0 and len(price[0])!=0 and len(quant[0])!=0):
		#data=market_crop_price.objects.filter('price_per_kg'>=price and 'market_id_capacity'>=quant).select_related('market_id')
		data=market_crop_price.objects.raw('select * from market_market_crop_price,market_market where market_id_id in (select id from market_market where capacity >=%s) and price_per_kg >=%s ',[quant[0],price[0]])
		return data
	if(len(loc[0])==0 and len(crop[0])!=0 and len(price[0])==0 and len(quant[0])==0):
		data=market_crop_price.objects.raw('select * from market_market_crop_price,market_market where crop_id_id in (select id from crop_warehouse_crop where crop_name=%s)',crop)
		return data
	if(len(loc[0])==0 and len(crop[0])!=0 and len(price[0])==0 and len(quant[0])!=0):
		data=market_crop_price.objects.raw('select * from market_market_crop_price,market_market where crop_id_id in (select id from crop_warehouse_crop where crop_name=%s) and market_id_id in (select id from market_market where capacity>=%s)',[crop[0],quant[0]])
		return data
	if(len(loc[0])==0 and len(crop[0])!=0 and len(price[0])!=0 and len(quant[0])==0):
		data=market_crop_price.objects.raw('select * from market_market_crop_price,market_market where crop_id_id=(select id from crop_warehouse_crop where crop_name=%s) and price_per_kg >=%s',[crop[0],price[0]])
		return data
	if(len(loc[0])==0 and len(crop[0])!=0 and len(price[0])!=0 and len(quant[0])!=0):
		data=market_crop_price.objects.raw('select * from market_market_crop_price,market_market where crop_id_id=(select id from crop_warehouse_crop where crop_name=%s) and price_per_kg >=%s and market_id_id in (select id from market_market where capacity>=%s)',[crop[0],price[0],quant[0]])
		return data
	if(len(loc[0])!=0 and len(crop[0])==0 and len(price[0])==0 and len(quant[0])==0):
		data=Market.objects.raw('select * from market_market where location =%s ',loc)
		return data
	if(len(loc[0])!=0 and len(crop[0])==0 and len(price[0])==0 and len(quant[0])!=0):
		data=Market.objects.raw('select * from market_market where location =%s and capacity >=%s ',[loc[0],quant[0]])
		return data
	if(len(loc[0])!=0 and len(crop[0])==0 and len(price[0])!=0 and len(quant[0])==0):
		data=market_crop_price.objects.raw('select * from market_market_crop_price,market_market where market_id_id in(select id from market_market where location=%s) and price_per_kg >=%s ',[loc[0],price[0]])
		return data
	if(len(loc[0])!=0 and len(crop[0])==0 and len(price[0])!=0 and len(quant[0])!=0):
		data=market_crop_price.objects.raw('select * from market_market_crop_price,market_market where market_id_id in(select id from market_market where location=%s and capacity>=%s)  and price_per_kg >=%s ',[loc[0],quant[0],price[0]])
		return data
	if(len(loc[0])!=0 and len(crop[0])!=0 and len(price[0])==0 and len(quant[0])==0):
		data=market_crop_price.objects.raw('select * from market_market_crop_price,market_market where market_id_id in (select id from market_market where location=%s) and crop_id_id in (select id from crop_warehouse_crop where crop_name=%s)',[loc[0],crop[0]])
		return data
	if(len(loc[0])!=0 and len(crop[0])!=0 and len(price[0])==0 and len(quant[0])!=0):
		data=market_crop_price.objects.raw('select * from market_market_crop_price,market_market where market_id_id in (select id from market_market where location=%s and capacity>=%s) and crop_id_id=(select id from crop_warehouse_crop where crop_name=%s)',[loc[0],quant[0],crop[0]])
		return data
	if(len(loc[0])!=0 and len(crop[0])!=0 and len(price[0])!=0 and len(quant[0])==0):
		data=market_crop_price.objects.raw('select * from market_market_crop_price,market_market where market_id_id in (select id from market_market where location=%s) and crop_id_id in (select id from crop_warehouse_crop where crop_name=%s) and price_per_kg >=%s ',[loc[0],crop[0],price[0]])
		return data
	

	if(len(loc[0])!=0 and len(crop[0])!=0 and len(price[0])!=0 and len(quant[0])!=0):
		data=Market.objects.raw('select * from market_market_crop_price,,market_market where market_id_id in (select id from market_market where location=%s and capacity>=%s)  and price_per_kg >=%s and crop_id_id in (select id from crop_warehouse_crop where crop_name=%s)',[loc[0],quant[0],price[0],crop[0]])
		return data
	else:
		return []
	return []



