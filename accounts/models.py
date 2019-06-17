from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.core import validators
import re

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Apelido/Usuario', max_length=30, unique=True, validators=[
        validators.RegexValidator(
            re.compile('^[\w.@+-]+$'),
            'Informe nome de usuário válido.'
            'Este valor deve conter apenas letra, números'
            'e os caracteres: @ . + - _'
            'invalid'
        )
    ], help_text='Um nome curso que será utilizado para identificar-lhe na plataforma.')
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email', unique=True)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de cadastro', auto_now_add=True)

    USERNAME_FIELD ='username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]