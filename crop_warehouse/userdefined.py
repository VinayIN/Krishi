from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from models import Crop,Warehouse

def processQuery1(loc,cap,cha):
	if(len(loc[0])!=0 and len(cap[0])==0 and len(cha[0])==0):
		data=Warehouse.objects.raw('select * from crop_warehouse_warehouse where location =%s',loc)
		return data
	if(len(loc[0])==0 and len(cap[0])!=0 and len(cha[0])==0):
		data=Warehouse.objects.raw('select * from crop_warehouse_warehouse where capacity >=%s',cap)
		return data
	if(len(loc[0])==0 and len(cap[0])==0 and len(cha[0])!=0):
		data=Warehouse.objects.raw('select * from crop_warehouse_warehouse where price <=%s',cha)
		return data
	if(len(loc[0])==0 and len(cap[0])!=0 and len(cha[0])!=0):
		data=Warehouse.objects.raw('select * from crop_warehouse_warehouse where price <=%s and capacity >=%s',[cha[0],cap[0]])
		return data
	if(len(loc[0])!=0 and len(cap[0])==0 and len(cha[0])!=0):
		data=Warehouse.objects.raw('select * from crop_warehouse_warehouse where price <=%s and location=%s',[cha[0],loc[0]])
		return data
	if(len(loc[0])!=0 and len(cap[0])!=0 and len(cha[0])==0):
		data=Warehouse.objects.raw('select * from crop_warehouse_warehouse where location =%s and capacity >=%s',[loc[0],cap[0]])
		return data
	if(len(loc[0])!=0 and len(cap[0])!=0 and len(cha[0])!=0):
		data=Warehouse.objects.raw('select * from crop_warehouse_warehouse where location =%s and capacity >=%s and price <=%s',[loc[0],cap[0],cha[0]])
		return data
	else:
		return []
	return []



def processQuery2(cat,price):
	if(len(cat[0])!=0 and len(price[0])==0 ):
		data=Warehouse.objects.raw('select * from crop_warehouse_crop where catagory =%s',cat)
		return data
	if(len(cat[0])==0 and len(price[0])!=0):
		data=Warehouse.objects.raw('select * from crop_warehouse_crop where crop_price_cur >=%s',price)
		return data
	
	if(len(cat[0])!=0 and len(price[0])!=0):
		data=Warehouse.objects.raw('select * from crop_warehouse_crop where catagory =%s and crop_price_cur >=%s ',[cat[0],price[0]])
		return data
	else :
		return []

	return []



