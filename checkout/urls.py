from django.conf.urls import url
from django.urls import path
from .views import CreateCartItemView, CartItemView, CheckoutView, OrderListView, OrderDetailView, PaypalView

app_name = 'checkout'

urlpatterns = [
    url(r'^carrinho/adicionar/(?P<slug>[\w_-]+)/$', CreateCartItemView.as_view(), name='create_cartitem'),
    path('carrinho/', CartItemView.as_view(), name='cart_item'),
    path('finalizando/', CheckoutView.as_view(), name='checkout'),
    path('meus-pedidos/', OrderListView.as_view(), name='order_list'),
    url(r'^meus-pedidos/(?P<pk>\d+)/$', OrderDetailView.as_view(), name='order_detail'),
    url(r'^finalizando/(?P<pk>\d+)/paypal/$', PaypalView.as_view() , name='paypal_view'),
]
