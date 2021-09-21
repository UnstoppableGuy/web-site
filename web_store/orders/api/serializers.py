from rest_framework import serializers
from orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('email', 'address', 'city', 'paid', 'created', 'updated', 'first_name', 'last_name', 'user')