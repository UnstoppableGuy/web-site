from django.db import models
from first_app.models import Product
from django.conf import settings
from decimal import Decimal
from coupons.models import Coupon
from django.core.validators import MinValueValidator, MaxValueValidator

class Order(models.Model):
    '''
    user not required, there can be an anonimous.
    if user is deleted the order will not changed.
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    '''
    Храним также купон в заказе для дальнейшего просмотра и в независимости от заказа 
    чтобы в дальнейшем при удалении/изменении купона заказ остался бы прежним.
    '''
    coupon = models.ForeignKey(Coupon, related_name='orders', null=True, blank=True, on_delete=models.CASCADE)                                
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        total_cost_after_discount = total_cost - total_cost * (self.discount / Decimal('100'))
        return total_cost_after_discount

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity