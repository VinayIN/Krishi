from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.Home_Page, name='index'),
    url(r'^view_report$',views.Gen_Report, name='report'),

]
