from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^orders/$', views.OrderListView.as_view(), name='order_list'),
    url(r'^orders/(?P<pk>\d+)/$', views.OrderDetailView.as_view(), name='order_detail'),
]