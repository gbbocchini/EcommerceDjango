from .views import RegisterView, IndexAccounts, UpdateUserView, UpdatePasswordView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('', IndexAccounts.as_view(), name='index_accounts'),
    path('registro/', RegisterView.as_view(), name='register'),
    path('alterar-dados/', UpdateUserView.as_view(), name='update_user'),
    path('alterar-senha/', UpdatePasswordView.as_view(), name='update_password'),

]
