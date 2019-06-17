from django.urls import path
from django.conf.urls import url
from .views import ProductList, CategoryView
from .views import product

app_name = 'catalogo'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    url(r'^(?P<slug>[\w_-]+)/$', CategoryView.as_view(), name='category'),
    url(r'^produtos/(?P<slug>[\w_-]+)/$', product, name='product'),
]