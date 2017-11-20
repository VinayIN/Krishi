# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from models import Market,market_crop_price
from tables import MarketTable,market_crop_priceTable

# Create your views here.
from django.http import HttpResponse

from django_tables2 import RequestConfig
from .userdefined import processQuery

def homepage(request):
        return render(request,'market_query_page.html')

def generate_report(request):
    if(request.method == "POST"):
        loc=[]
        crop=[]
        price=[]
        quant=[]
        loc=request.POST.get('location').split(',')
        crop=request.POST.get('crops').split(',')
        price=request.POST.get('price').split(',')
        quant=request.POST.get('quantity').split(',')
        #data=Market.objects.raw('select id,pincode from market_market where location=%s',[var[0]])
        data=processQuery(loc,crop,price,quant)

        tableMarket=MarketTable(data)
        RequestConfig(request).configure(tableMarket)

        tableMarket_Crop_Price=market_crop_priceTable(data)
        RequestConfig(request).configure(tableMarket_Crop_Price)
        context={"t_records": [1], "tableMarket": tableMarket , "tableMarket_Crop_Price": tableMarket_Crop_Price}
    else:
		return render(request,'market_query_page.html')
    return render(request,"market_report_page.html",context)


