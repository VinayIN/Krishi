from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from models import Transportation

def processQuery(loc,cap,trip):
	if(len(loc[0])!=0 and len(cap[0])==0 and len(trip[0])==0):
		data=Transportation.objects.raw('select * from transport_transportation where location =%s',loc)
		return data
	if(len(loc[0])==0 and len(cap[0])!=0 and len(trip[0])==0):
		data=Transportation.objects.raw('select * from transport_transportation where capacity_per_person >=%s',cap)
		return data
	if(len(loc[0])==0 and len(cap[0])==0 and len(trip[0])!=0):
		data=Transportation.objects.raw('select * from transport_transportation where trip_price_per_km <=%s',trip)
		return data
	if(len(loc[0])==0 and len(cap[0])!=0 and len(trip[0])!=0):
		data=Transportation.objects.raw('select * from transport_transportation where trip_price_per_km <=%s and capacity_per_person >=%s',[trip[0],cap[0]])
		return data
	if(len(loc[0])!=0 and len(cap[0])==0 and len(trip[0])!=0):
		data=Transportation.objects.raw('select * from transport_transportation where trip_price_per_km <=%s and location=%s',[trip[0],loc[0]])
		return data
	if(len(loc[0])!=0 and len(cap[0])!=0 and len(trip[0])==0):
		data=Transportation.objects.raw('select * from transport_transportation where location =%s and capacity_per_person >=%s',[loc[0],cap[0]])
		return data
	if(len(loc[0])!=0 and len(cap[0])!=0 and len(trip[0])!=0):
		data=Transportation.objects.raw('select * from transport_transportation where location =%s and capacity_per_person >=%s and trip_price_per_km <=%s',[loc[0],cap[0],trip[0]])
		return data
	else:
		return []

	return []



