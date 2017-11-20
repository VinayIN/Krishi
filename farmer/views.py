# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth import login,authenticate
from farmer.forms import SignUpForm,ProfileForm #,CropForm,MarketForm,WarehouseForm,TransportForm
from django.views.generic import ListView
from django.contrib.auth import update_session_auth_hash
import sys
sys.path.append("../")
from .models import Profile
from market.models import Market
from transport.models import Transportation
from crop_warehouse.models import Crop,Warehouse



@login_required
@transaction.atomic
def homepage(request):
	return render(request, 'homepage.html')

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            if form.is_valid():
                user=form.save()
                user.refresh_from_db()  
                user.first_name=form.cleaned_data.get('first_name')
                user.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)
                return redirect('home')
    else:
            form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
@login_required(login_url = '/login')
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = SignUpForm(data=request.POST, instance=request.user)
        profile_form = ProfileForm(data=request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            
            user=user_form.save()
            pw = user.password
                        # thus we need to use set password to encrypt the password string
            update_session_auth_hash(request,user)
            user.save()
            profile=profile_form.save()
            profile.user = user
            profile.save()
            #update_session_auth_hash(request, user)
            
            
        
            messages.success(request,'Your profile was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = SignUpForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

