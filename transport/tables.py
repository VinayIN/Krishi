import django_tables2 as tables 
from .models import Transportation

class TransportationTable(tables.Table):
	class Meta:
		model= Transportation
		template= 'django_tables2/bootstrap.html'

