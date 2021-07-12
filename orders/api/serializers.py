from rest_framework import serializers
from ..models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['id', 'owner', 'archived', 'created', 'modified']


class OrderSerializer(serializers.ModelSerializer):
    orderitem_set = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'owner', 'orderitem_set', 'status', 'archived', 'created', 'modified',]
