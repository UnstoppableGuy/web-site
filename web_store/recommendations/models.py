from django.db import models
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from first_app.models import Product
from orders.models import OrderItem

class StatisticsItem(models.Model): # pragma: no cover
    '''
    - Сохраняет статистику пользователя на сайте.
    - Создается/Удаляется автоматически при создании/удалении пользователя   
    - Обновляется массив продуктов при удалении/добавлении продуктов.
    - Обновляются все статистические поля при соответствующих действиях пользователя.    
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    clicks = models.IntegerField(default=0, validators=[MinValueValidator(0)])    
    times_was_in_orders = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    amount_was_in_orders = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    '''
    При создании передается обьект пользователя,
    опираясь на обьект пользователся заполнчются 
    все продукты и дефолтные клики.
    '''    
    @staticmethod
    def create_for_user(user):
        all_user_statistics_items = []
        all_products = Product.objects.all()        
        for pr in all_products:            
            new_item = StatisticsItem.objects.create(user=user, product=pr)
            all_user_statistics_items.append(new_item)
        return all_user_statistics_items
    
    @staticmethod
    def get_all_items_for_user(user):
        all_items = StatisticsItem.objects.filter(user=user)
        return all_items

    # just adds new product to all of users.
    @staticmethod
    def add_new_product(product):
        users = User.objects.all()
        for user in users:
            if not StatisticsItem.objects.filter(user=user).exists():
                StatisticsItem.create_for_user(user)
            elif not StatisticsItem.objects.filter(user=user).filter(product=product).exists():
                StatisticsItem.objects.create(user=user, product=product)
            else:
                raise Exception('Was going on? That is impossible dude!')
    
    @staticmethod
    def add_click(user, product, amount=1):
        item = StatisticsItem.objects.get(user=user, product=product)
        item.clicks += amount
        item.save()
        return item

    @staticmethod
    def add_times_was_in_order(user, product, amount=1):
        item = StatisticsItem.objects.get(user=user, product=product)
        item.times_was_in_orders += amount
        item.save()
        return item

    @staticmethod
    def add_amount_was_in_order(user, product, amount=1):
        item = StatisticsItem.objects.get(user=user, product=product)
        item.amount_was_in_orders += amount
        item.save()
        return item

    def __str__(self):
        return f'User: {self.user} | ' + f'Product: {self.product}'
    
# User addin.
@receiver(post_save, sender=User)
def create_statistics_item(sender, instance, created, **kwargs):
    if created:                
        StatisticsItem.create_for_user(user=instance)

# Product adddin.
@receiver(post_save, sender=Product)
def add_new_product_to_all_statistics_items(sender, instance, created, **kwargs):
    if created:
        StatisticsItem.add_new_product(product=instance)

# OrderItem addin.
@receiver(post_save, sender=OrderItem) # pragma: no cover
def add_times_was_in_orders(sender, instance, created, **kwargs):
    if created:     
        if instance.order.user != None:
            StatisticsItem.add_times_was_in_order(
                user=instance.order.user,
                product=instance.product)
            StatisticsItem.add_amount_was_in_order(
                user=instance.order.user,
                product=instance.product
            )
        

        