from django import forms

'''
Generete amount of products user could choice. [0, 19].
or [0, product.quantity]
'''
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(20)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    # False - добавить кол-во товара к существующему.
    # True  - замеенить существующие значение.
    update_quantity = forms.BooleanField(required=False, initial=True, widget=forms.HiddenInput)