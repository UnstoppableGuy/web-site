from django.conf.urls import url, re_path
from . import views


urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    re_path(r'^order/(?P<order_id>\d+)/$', views.order_specific, name='order_specific'),
    re_path(r'^all-orders/$', views.order_all, name='order_all'),
]