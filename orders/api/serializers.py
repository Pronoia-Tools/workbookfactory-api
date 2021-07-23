from rest_framework import serializers
from djmoney.contrib.django_rest_framework import MoneyField
from ..models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    price = MoneyField(max_digits=10, decimal_places=2)

    class Meta:
        model = OrderItem
        fields = ['id', 'owner', 'archived', 'created', 'price', 'quantity', 'modified']


class OrderSerializer(serializers.ModelSerializer):
    orderitem_set = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'owner', 'orderitem_set', 'status', 'archived', 'created', 'modified',]
