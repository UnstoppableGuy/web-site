from django.test import TestCase
from django import forms
from cart.forms import CartAddProductForm


class CartAddProductFormTest(TestCase):

    def test_quantity_coerce_int(self):
        form = CartAddProductForm()
        self.assertTrue(form.fields['quantity'].coerce == int)

    def test_update_quantity_required_false(self):
        form = CartAddProductForm()
        self.assertTrue(form.fields['update_quantity'].required == False)

    def test_update_quantity_initial(self):
        form = CartAddProductForm()
        self.assertTrue(form.fields['update_quantity'].initial == True)    