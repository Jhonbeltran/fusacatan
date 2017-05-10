from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^zone/$', views.ZoneList.as_view(), name='zone'),
	url(r'^zone/(?P<pk>[0-9]+)/$', views.ZoneDetail.as_view(),
		name='detail'),
	url(r'^zone/new$', views.ZoneCreate.as_view(), name='new'),
	url(r'^zone/edit/(?P<pk>[0-9]+)/$',
		views.ZoneUpdate.as_view(), name='edit'),
    url(r'^zone/delete/(?P<pk>[0-9]+)/$',
    	views.ZoneDelete.as_view(), name='delete'),
]