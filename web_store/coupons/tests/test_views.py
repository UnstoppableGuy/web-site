from django.test import TestCase
from django.urls import reverse # for accessin urls by their names.
from coupons.models import Coupon
# from django.test.client import RequestFactory

class CouponApplyViewTest(TestCase):

    @classmethod
    def setUpTestData(self):
        Coupon.objects.create(code='kek')
        # self.factory = RequestFactory()

    def test_view_url_exists_atdesired_location(self):
        resp = self.client.post('/coupons/apply/')
        self.assertEquals(resp.status_code, 302)

    def test_view_url_accessible_by_name(self):
        resp = self.client.post(reverse('coupons:coupon_apply'))
        self.assertEqual(resp.status_code, 302)

    # def test_view_with_data_from_form(self):
    #     coupon = Coupon.objects.get(code='kek')
    #     request = self.factory.post('coupons:coupon_apply', {'code': coupon.code})
    #     self.assertEqual(request.session['coupon_id'], coupon.id)
