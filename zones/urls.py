from django.conf.urls import url
from . import views

# urlpatterns = [
# 	url(r'^zone/$', views.zoneList.as_view(), name='zone'),
# 	url(r'^zone/(?P<pk>[0-9]+)/$', views.zoneDetail.as_view(),
# 		name='detail'),
# 	url(r'^zone/new$', views.zoneCreate.as_view(), name='new'),
# 	url(r'^zone/edit/(?P<pk>[0-9]+)/$',
# 		views.zoneUpdate.as_view(), name='edit'),
#     url(r'^zone/delete/(?P<pk>[0-9]+)/$',
#     	views.zoneDelete.as_view(), name='delete'),
# ]