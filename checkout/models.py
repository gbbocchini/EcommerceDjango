from django.db import models
from catalogo.models import Product
from django.conf import settings
from pagseguro import PagSeguro


class CartItemManager(models.Manager):

    def add_item(self, cart_key, product):
        if self.filter(cart_key=cart_key, product=product).exists():
            created = False
            cart_item = self.get(cart_key=cart_key, product=product)
            cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
        else:
            created = True
            cart_item = CartItem.objects.create(cart_key=cart_key, product=product, price=product.price)
        return cart_item, created



class CartItem(models.Model):
    cart_key = models.CharField('Chave carrinho', max_length=40, db_index=True)
    product = models.ForeignKey(Product, verbose_name='Produto', on_delete='SET_NULL')
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    objects = CartItemManager()

    class Meta:
        verbose_name = 'Item do carrinho'
        verbose_name_plural = 'Itens dos carrinhos'
        unique_together = (('cart_key', 'product'),)


    def __str__(self):
        return '{} [{}]'.format(self.product, self.quantity)


# signal para qdo um item do carrinho seja setado para 0 (apaga automaticamente item)
def post_save_cart_item(instance, **kwargs):
    if instance.quantity < 1:
        instance.delete()


models.signals.post_save.connect(post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item')


class OrderManager(models.Manager):

    def create_order(self, user, cart_items):
        order = self.create(user=user)
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(order=order, quantity=cart_item.quantity, product = cart_item.product, price=cart_item.price)
        return order


class Order(models.Model):
    STATUS_CHOISES = (
        (0, 'Aguardando Pagamento'),
        (1, 'Concluída'),
        (3, 'Cancelada'),
    )

    PAYMENT_OPTION_CHOICES = (
        ('deposit', 'Depósito'),
        ('pagseguro','PagSeguro'),
        ('paypal', 'PayPal'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', on_delete='SET_NULL')
    status = models.IntegerField('Situação', choices=STATUS_CHOISES, default=0, blank=True)
    payment_option = models.CharField('Opção de pagamento', choices=PAYMENT_OPTION_CHOICES, max_length=20, default='deposit')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Alterado em', auto_now=True)

    objects = OrderManager()

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def products(self):
        products_ids = self.items.values_list('product')
        return Product.objects.filter(pk__in=products_ids)

    def total(self):
        aggregate_queryset = self.items.aggregate(total=models.Sum(models.F('price')*models.F('quantity'), output_field=models.DecimalField()))
        return aggregate_queryset['total']


    def complete(self):
        self.status = 1
        self.save()


    def paypal(self):
        self.payment_option = 'paypal'
        self.save()
        paypal_dict = {
            'upload': '1',
            'business': settings.PAYPAL_EMAIL,
            'invoice': self.pk,
            'cmd': '_cart',
            'currency_code': 'BRL',
            'charset': 'utf-8',
        }
        index = 1
        for item in self.items.all():
            paypal_dict['amount_{}'.format(index)] = '%.2f' % item.price
            paypal_dict['item_name_{}'.format(index)] = item.product.name
            paypal_dict['quantity_{}'.format(index)] = item.quantity
            index = index + 1
        return paypal_dict


    def __str__(self):
        return 'Pedido #{}'.format(self.pk)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='Pedido', related_name='items', on_delete='SET_NULL')
    product = models.ForeignKey('catalogo.Product', verbose_name='Produto', on_delete='SET_NULL')
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens dos pedidos'

    def __str__(self):
        return '[{}] {}'.format(self.order, self.product)

