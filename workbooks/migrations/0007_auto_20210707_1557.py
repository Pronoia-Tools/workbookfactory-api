# Generated by Django 3.2.4 on 2021-07-07 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workbooks', '0006_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='title',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='back_matter',
        ),
        migrations.RemoveField(
            model_name='question',
            name='content',
        ),
        migrations.RemoveField(
            model_name='question',
            name='front_matter',
        ),
        migrations.RemoveField(
            model_name='question',
            name='slug',
        ),
    ]
