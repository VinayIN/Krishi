import django_tables2 as tables 
from .models import Crop,Warehouse

class CropTable(tables.Table):
	class Meta:
		model= Crop
		template= 'django_tables2/bootstrap.html'

class WarehouseTable(tables.Table):
	class Meta:
		model= Warehouse
		template= 'django_tables2/bootstrap.html'