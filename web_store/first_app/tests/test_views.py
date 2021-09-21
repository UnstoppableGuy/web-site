from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse # for accessin urls by their names.
from first_app.models import Product, Category

class GetAboutUsViewTest(TestCase):

    # 1)
    def test_view_url_exists_atdesired_location(self):
        resp = self.client.get('/about_us/')
        self.assertEquals(resp.status_code, 200)

    # 2)
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('about_us_url'))
        self.assertEqual(resp.status_code, 200)
    
    # 3)
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('about_us_url'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'first_app/about_us.html')


class GetSpecificProductViewTest(TestCase):

    @classmethod
    def setUpTestData(self):
        # create 4 products.
        number_of_products = 3        
        for product_num in range(number_of_products):
            Product.objects.create(title=f'my_product-{product_num}', category=Category.objects.create(title=f'Category-{product_num}'))
    
    def test_view_url_exists_atdesired_location(self):
        resp = self.client.get(f'/products/{Product.objects.get(title="my_product-0")}/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('specific_product_url_with_slug', args=[Product.objects.get(title='my_product-0')]))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('specific_product_url_with_slug', args=[Product.objects.get(title='my_product-0')]))        
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'first_app/specific_product.html')

class GetUserProfilePageViewTest(TestCase):

    def setUp(self):
        # Create 2 users
        test_user1 = User.objects.create(username='testuser1', password='12345')        
        test_user1.save()
        test_user2 = User.objects.create(username='testuser2', password='123456')        
        test_user2.save()

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('user_profile_url'))
        self.assertRedirects(resp, '/')    