from django.test import TestCase
from coupons.models import Coupon


class CouponModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods    
        Coupon.objects.create(code='qwerty123456__aba')

    def test_code_max_length(self):
        coupon = Coupon.objects.get(pk=1)
        max_length = coupon._meta.get_field('code').max_length
        self.assertEquals(max_length, 50)

    def test_code_unique(self):
        coupon = Coupon.objects.get(pk=1)
        unique = coupon._meta.get_field('code').unique
        self.assertEquals(unique, True)

    def test_valid_from_auto_now_add(self):
        coupon = Coupon.objects.get(pk=1)
        auto_now_add = coupon._meta.get_field('valid_from').auto_now_add
        self.assertEquals(auto_now_add, True)

    def test_valid_to_auto_now_add(self):
        coupon = Coupon.objects.get(pk=1)
        auto_now_add = coupon._meta.get_field('valid_to').auto_now_add
        self.assertEquals(auto_now_add, True)

    def test_discount_default_is_zero(self):
        coupon = Coupon.objects.get(pk=1)
        default = coupon._meta.get_field('discount').default
        self.assertEquals(default, 0)

    def test_active_default_false(self):
        coupon = Coupon.objects.get(pk=1)
        default = coupon._meta.get_field('active').default
        self.assertEquals(default, False)

    def test_string_is_code(self):
        coupon = Coupon.objects.get(pk=1)
        string = coupon.__str__()
        self.assertEquals('qwerty123456__aba', string)