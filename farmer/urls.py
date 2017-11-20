from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView,ListView

urlpatterns=[
	url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
	url(r'^home$', views.homepage, name='home'),
	url(r'^logout$', auth_views.logout, {'next_page': 'login'}, name='logout'),
	url(r'^signup$', views.signup, name='signup'),
	url(r'^profile$', views.update_profile, name='update_profile'),

]