from django.test import TestCase
from django.contrib.auth.models import User
from first_app.models import Category, Product, Wallet, Profile

'''
class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_true_is_false(self):
        print("Method: test_true_is_false.")
        self.assertFalse(True)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
'''

class CategoryModelTest(TestCase):  

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods    
        Category.objects.create(title='Cars', pk=1)

    def test_title_label(self):
        category = Category.objects.get(pk=1)
        field_label = category._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')
    
    def test_slug_label(self):
        category = Category.objects.get(pk=1)
        field_label = category._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')

    def test_image_label(self):
        category = Category.objects.get(pk=1)
        field_label = category._meta.get_field('image').verbose_name
        self.assertEquals(field_label, "Изображение")

    def test_title_max_length(self):
        category = Category.objects.get(pk=1)
        max_length = category._meta.get_field('title').max_length
        self.assertEquals(max_length, 50)
    
    def test_slug_max_length(self):
        category = Category.objects.get(pk=1)
        max_length = category._meta.get_field('slug').max_length
        self.assertEquals(max_length, 50)

class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods            
        Product.objects.create(title='Computer_1', category=Category.objects.create(title='Computers'))

    def test_title_label(self):
        product = Product.objects.get(pk=1)
        field_label = product._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Name')
    
    def test_description_label(self):
        product = Product.objects.get(pk=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Description')

    def test_price_max_digits(self):
        product = Product.objects.get(pk=1)
        max_digits = product._meta.get_field('price').max_digits
        self.assertEquals(max_digits, 9)

    def test_image_label(self):
        product = Product.objects.get(pk=1)
        field_label = product._meta.get_field('image').verbose_name
        self.assertEquals(field_label, "Изображение")

    def test_slug_max_length(self):
        product = Product.objects.get(pk=1)
        max_length = product._meta.get_field('slug').max_length
        self.assertEquals(max_length, 50)

class WalletModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods    
        User.objects.create(username='Misha', first_name='Misha')

    def test_balance_max_digits(self):
        wallet = Wallet.objects.get(user=User.objects.get(username='Misha'))
        max_digits = wallet._meta.get_field('balance').max_digits
        self.assertEquals(max_digits, 9)

    def test_get_balance(self):
        wallet = Wallet.objects.get(user=User.objects.get(username='Misha'))        
        self.assertEquals(wallet.get_balance(), str(wallet.balance)+'$')
    
    def test_object_name_is_username_and_wallet(self):
        wallet = Wallet.objects.get(user=User.objects.get(username='Misha'))        
        expected_object_name = wallet.user.username + "_wallet"
        self.assertEquals(expected_object_name, str(wallet))

class ProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods    
        User.objects.create(username='Misha')

    def test_phone_number_max_length(self):
        profile = Profile.objects.get(user=User.objects.get(pk=1))
        max_length = profile._meta.get_field('phone_number').max_length
        self.assertEquals(max_length, 12)

    def test_address_max_length(self):
        profile = Profile.objects.get(user=User.objects.get(pk=1))
        max_length = profile._meta.get_field('address').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_username_and_profile(self):
        profile = Profile.objects.get(user=User.objects.get(pk=1))
        expected_object_name = profile.user.username + '_profile'
        self.assertEquals(expected_object_name, str(profile))