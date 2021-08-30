from django.db.models.signals import post_save
from django.dispatch import receiver
from workbooks.models import Workbook
from djstripe.models import Product, Price
import djstripe.models
import djstripe.settings

import stripe

@receiver(post_save, sender=Workbook)
def create_stripe_product(sender, instance, created, **kwargs):
    if created:
        stripe_product_data = stripe.Product.create(
            api_key=djstripe.settings.STRIPE_SECRET_KEY,
            name=instance.title
        )


        stripe_price_data = stripe.Price.create(
            api_key=djstripe.settings.STRIPE_SECRET_KEY,
            unit_amount_decimal=instance.price.amount,
            currency="usd",
            product=stripe_product_data["id"]
        )

        stripe_product = Product.sync_from_stripe_data(stripe_product_data)
        stripe_price = Price.sync_from_stripe_data(stripe_price_data)

        instance.stripe_product_id = stripe_product.djstripe_id
        instance.stripe_price_id = stripe_price.djstripe_id
        instance.save()

        return
