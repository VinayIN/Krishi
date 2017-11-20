from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,market_crop_price
import sys
sys.path.append("../")
from market.models import Market
from transport.models import Transportation
from crop_warehouse.models import Crop,Warehouse




class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', )

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('address','pin','aadhar','crops','warehouses','markets','transportation')



class CropForm(forms.Form):
    crop=forms.ModelChoiceField(Crop)
class WarehouseForm(forms.Form):
    warehouse=forms.ModelChoiceField(Warehouse)
    max_price_kg=forms.IntegerField(help_text='enter the max price you can pay for 1 kg of storage')
    location=forms.CharField(max_length=20,help_text='enter it if you dont know the warehouse name')
class MarketForm(forms.Form):
    market=forms.ModelChoiceField(Market)
    max_price_kg=forms.IntegerField(help_text='enter the min price you wish to get for 1 kg of storage')
    location=forms.CharField(max_length=20,help_text='enter it if you dont know the market name')
    pincode=forms.IntegerField()
class TransportForm(forms.Form):
    market=forms.ModelChoiceField(Transportation)
    trip_price_kg=forms.IntegerField(help_text='enter the min price you pay to get for 1 kg of storage')
    location=forms.CharField(max_length=20,help_text='enter it if you dont know the transport name')
    pincode=forms.IntegerField()
