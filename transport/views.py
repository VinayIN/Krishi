# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from models import Transportation
from tables import TransportationTable

# Create your views here.
from django.http import HttpResponse

from django_tables2 import RequestConfig
from .userdefined import processQuery


def Home_Page(request):
        return render(request,'query_page.html')

def Gen_Report(request):
    if(request.method == "POST"):
        loc=[]
        cap=[]
        trip=[]
        loc=request.POST.get('location').split(',')
        cap=request.POST.get('capacity').split(',')
        trip=request.POST.get('trip_price').split(',')
        data=processQuery(loc,cap,trip)
        tableTransport=TransportationTable(data)
        RequestConfig(request).configure(tableTransport)
        context={"t_records": [1], "tableTransport": tableTransport}
    else:
		return render(request,'query_page.html')
    return render(request,"report_page.html",context)


