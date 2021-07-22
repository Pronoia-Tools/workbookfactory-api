# Generated by Django 3.2.4 on 2021-07-22 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_account_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_accounts', to=settings.AUTH_USER_MODEL),
        ),
    ]
