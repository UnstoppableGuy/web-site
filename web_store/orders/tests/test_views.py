# from django.test import TestCase
# from django.urls import reverse # for accessin urls by their names.
# from orders.models import Order
# from django.contrib.auth import get_user_model
# from coupons.models import Coupon
# from django.contrib.auth import authenticate, login, logout

# User = get_user_model()

# class OrderAllViewTest(TestCase):

#     @classmethod
#     def setUpTestData(self):     
#         user = User.objects.create(username='MAkd', password='sdfsdfjw3432')
#         request = self.client.get('/orders/all-orders/')
#         user = authenticate(request, username=username, password=password)   
#         Coupon.objects.create(code='kek')
#         coupon = Coupon.objects.get(code='kek')
#         Order.objects.create(
#             first_name='sdf', 
#             last_name='sdfg', 
#             email='sdfs', 
#             address='sfhfgn', 
#             postal_code='sdfsg', 
#             city='sef', 
#             coupon=coupon)

#     def test_view_url_exists_atdesired_location(self):
#         resp = self.client.get('/orders/all-orders/')
#         self.assertEquals(resp.status_code, 200)

#     def test_view_url_accessible_by_name(self):
#         resp = self.client.get(reverse('orders:order_all'))
#         self.assertEqual(resp.status_code, 200)


# class OrderSpecificViewTest(TestCase):

#     @classmethod
#     def setUpTestData(self):        
#         Coupon.objects.create(code='kek')
#         Order.objects.create(
#             first_name='sdf', 
#             last_name='sdfg', 
#             email='sdfs', 
#             address='sfhfgn', 
#             postal_code='sdfsg', 
#             city='sef', 
#             coupon=Coupon.objects.get(code='kek'))

#     def test_view_url_exists_atdesired_location(self):
#         resp = self.client.get(f'/orders/order_specific/{Order.objects.get(pk=1)}/')
#         self.assertEquals(resp.status_code, 200)

#     def test_view_url_accessible_by_name(self):
#         resp = self.client.get(reverse('orders:order_specific', args=[Order.objects.get(pk=1)]))
#         self.assertEqual(resp.status_code, 200)