# Generated by Django 3.2.4 on 2021-07-20 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workbooks', '0012_remove_question_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='chapter',
            field=models.ManyToManyField(blank=True, to='workbooks.Chapter'),
        ),
    ]