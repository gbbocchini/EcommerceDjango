from django.db import models

class ContatoForm(models.Model):
    name = models.CharField('Nome', max_length=100, blank=False)
    email = models.EmailField('Email', blank=False)
    mensagem = models.TextField('Mensagem', max_length=200, blank=False)

    def __str__(self):
        return self.name
