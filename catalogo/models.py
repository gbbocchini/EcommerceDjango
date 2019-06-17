from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField('Nome', max_length=150, blank=False)
    slug = models.SlugField('Identificador', max_length=100)
    created = models.DateTimeField('Criado em:', auto_now_add=True)
    modified = models.DateTimeField('Alterado em:', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Categoria', on_delete='CASCADE')
    name = models.CharField('Nome', max_length=150, blank=False)
    slug = models.SlugField('Identificador', max_length=100)
    created = models.DateTimeField('Criado em:', auto_now_add=True)
    modified = models.DateTimeField('Alterado em:', auto_now=True)
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=10)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalogo:product', kwargs={'slug':self.slug})