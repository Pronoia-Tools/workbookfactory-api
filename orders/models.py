from django.db import models
from django.utils.text import slugify
from djmoney.models.fields import MoneyField
from utils.models import Core

# Create your models here.
class Order(Core):
    ORDER_TYPE = (
        ("1", "Placed"),
        ("2", "In Process"),
        ("3", "Completed")
    )

    status = models.CharField(max_length=1, choices=ORDER_TYPE, default="1")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderItem(Core):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"
