from django.urls import path

from orders.views import (CanceledTemplateView, OrderCreateView,
                          OrderDetailView, OrderListView, SucessTemplateView)

app_name = 'orders'

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order_create'),
    path('', OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order'),
    path('order-sucess/', SucessTemplateView.as_view(), name='order_sucess'),
    path('order-canceled/', CanceledTemplateView.as_view(), name='order_canceled'),
]
