from django.test import TestCase
from django.urls import reverse # for accessin urls by their names.
from first_app.models import Product, Category

class CartAddViewTest(TestCase):

    @classmethod
    def setUpTestData(self):        
        Product.objects.create(title='test_title', pk=1, category=Category.objects.create(title='test_cat_title'))

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.post(f'/cart/add/{1}/')
        self.assertEquals(resp.status_code, 302)


class CartDetailViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.post(f'/cart/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cart:cart_detail'))
        self.assertEqual(resp.status_code, 200)


'''
class CartRemoveViewTest(TestCase):

    def test_view_url_accessible_by_name(self):
        resp = self.client.post(reverse('cart:cart_remove', args=(1,)))
        self.assertEqual(resp.status_code, 302)

'''