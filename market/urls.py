from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.homepage, name='index'),
    url(r'^view_report$',views.generate_report, name='report'),

]
