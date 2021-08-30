# Generated by Django 3.2.4 on 2021-08-30 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0008_2_5'),
        ('workbooks', '0022_alter_workbook_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='workbook',
            name='stripe_price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='djstripe.price'),
        ),
        migrations.AddField(
            model_name='workbook',
            name='stripe_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='djstripe.product'),
        ),
        migrations.AlterField(
            model_name='workbook',
            name='content',
            field=models.JSONField(blank=True, default={}),
        ),
    ]