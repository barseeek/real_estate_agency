# Generated by Django 3.2.23 on 2024-01-21 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20240121_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
