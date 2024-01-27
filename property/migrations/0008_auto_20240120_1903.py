# Generated by Django 3.2.23 on 2024-01-20 16:03

from django.db import migrations
import phonenumber_field.modelfields
import phonenumbers


def format_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    if flats.exists():
        for flat in flats.iterator():
            parsed_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
            if phonenumbers.is_valid_number(parsed_number):
                flat.owner_pure_phone = parsed_number
            else:
                flat.owner_pure_phone = None
            flat.save()

def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    if flats.exists():
        for flat in flats.iterator():
            flat.owner_pure_phone = None
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='RU', verbose_name='Нормализованный номер владельца'),
        ),
        migrations.RunPython(format_phonenumber, move_backward)
    ]
