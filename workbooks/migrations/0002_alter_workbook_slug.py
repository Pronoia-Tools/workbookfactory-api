# Generated by Django 3.2.4 on 2021-07-07 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workbooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workbook',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
    ]
