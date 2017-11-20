# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from models import Crop,Warehouse
from tables import CropTable,WarehouseTable

# Create your views here.
from django.http import HttpResponse

from django_tables2 import RequestConfig
from .userdefined import processQuery1,processQuery2

def Home_Page(request):
        return render(request,'crop_warehouse_query_page.html')

def Gen_Report(request):
    if(request.method == "POST"):
        cat=request.POST.get('catagory').split(',')
        loc=request.POST.get('location').split(',')
        cap=request.POST.get('capacity').split(',')
        cha=request.POST.get('charge').split(',')
        price=request.POST.get('price').split(',')
        #data=Crop.objects.raw('select id,crop_name from crop_warehouse_crop where catagory=%s',[var[0]])
        data=processQuery2(cat,price)
        tableCrop=CropTable(data)
        RequestConfig(request).configure(tableCrop)
        #data=Warehouse.objects.raw('select id,pincode from crop_warehouse_warehouse where location=%s',[ware[0]])
        data=processQuery1(loc,cap,cha)
        tableWarehouse=WarehouseTable(data)
        RequestConfig(request).configure(tableWarehouse)
        context={"t_records": [1], "tableCrop": tableCrop, "tableWarehouse": tableWarehouse}
    else:
		return render(request,'crop_warehouse_query_page.html')
    return render(request,"crop_warehouse_report_page.html",context)


