# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from cart.cart import Cart
# from first_app.models import Product, Category
# from django.test.client import RequestFactory

# User = get_user_model()

# class TestCart(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         Set up non-modified objects used by all test methods    
#         Category.objects.create(title='Cars', pk=1)
#         category = Category.objects.create(title='test_title_of_category')
#         product = Product.objects.create(title='test_product_title', category=category)    

#     def add_to_cart_test(self):
#         self.factory = RequestFactory()
#         product = Product.objects.get(title='test_title_of_category')
#         product_id = self.product.id
#         request = self.factory.post('cart:cart_add', {'product_id': product_id})
#         cart = Cart(request)
#         cart.add(product=product)
#         self.assertEquals(cart[product_id]['quantity'], 1)