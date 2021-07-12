from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import filters

from ..models import Order, OrderItem
from . import serializers


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # this will associate the owner of the object with the session user
    # def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # this will associate the owner of the object with the session user
    # def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)