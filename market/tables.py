import django_tables2 as tables 
from .models import Market,market_crop_price

class MarketTable(tables.Table):
	class Meta:
		model= Market
		template= 'django_tables2/bootstrap.html'

class market_crop_priceTable(tables.Table):
	class Meta:
		model= market_crop_price
		template='django_tables2/bootstrap.html'
