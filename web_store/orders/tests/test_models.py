from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
from orders.models import Order
from coupons.models import Coupon

class OrderModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods    
        Order.objects.create(
            user=User.objects.create(username='Misha'),
            first_name='d',
            last_name='kek',
            email='kekeke@gmail.com',
            address='dwer',
            postal_code='231',
            city='fef',
            coupon=Coupon.objects.create(code='sfsdf2'))

    def test_user_blank(self):
        order = Order.objects.get(pk=1)
        field_prop = order._meta.get_field('user').blank
        self.assertEquals(field_prop, True)

    def test_user_null(self):
        order = Order.objects.get(pk=1)
        field_prop = order._meta.get_field('user').null
        self.assertEquals(field_prop, True)

    def test_first_name_max_length(self):
        order = Order.objects.get(pk=1)
        field_prop = order._meta.get_field('first_name').max_length
        self.assertEquals(field_prop, 50)

    def test_last_name_max_length(self):
        order = Order.objects.get(pk=1)
        field_prop = order._meta.get_field('last_name').max_length
        self.assertEquals(field_prop, 50)

    def test_address_max_length(self):
        order = Order.objects.get(pk=1)
        field_prop = order._meta.get_field('address').max_length
        self.assertEquals(field_prop, 250)

    def test_postal_code_max_length(self):
        order = Order.objects.get(pk=1)
        field_prop = order._meta.get_field('postal_code').max_length
        self.assertEquals(field_prop, 20)

    def test_city_code_max_length(self):
        order = Order.objects.get(pk=1)
        field_prop = order._meta.get_field('city').max_length
        self.assertEquals(field_prop, 100)

    def test_created_auto_now_add(self):
        order = Order.objects.get(pk=1)
        field_prop = order._meta.get_field('created').auto_now_add
        self.assertEquals(field_prop, True)

    def test_updated_auto_now(self):
        order = Order.objects.get(pk=1)
        field_prop = order._meta.get_field('updated').auto_now
        self.assertEquals(field_prop, True)
        