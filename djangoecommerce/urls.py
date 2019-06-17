from django.contrib import admin
from django.urls import path, include
from core.views import Index, Contato, RegisterView
from django.contrib.auth import views as auth_views

app_name = 'djangoecommerce'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('catalogo/', include('catalogo.urls'), name='catalogo'),
    path('entrar/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('sair/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('conta/', include('accounts.urls'), name='accounts'),
    path('contato', Contato.as_view(), name='contato'),
    path('compras/', include('checkout.urls'), name='checkout'),
    path('paypal/', include('paypal.standard.ipn.urls')),
]
