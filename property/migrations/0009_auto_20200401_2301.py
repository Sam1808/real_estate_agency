# Generated by Django 2.2.4 on 2020-04-01 20:01
import phonenumbers
from django.db import migrations
from django.apps import apps

def normalize_owners_phone_number(apps, schema_editor):
    flats = apps.get_model('property', 'Flat')
    for flat in flats.objects.all():
        owners_phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(owners_phonenumber):
            flat.normalised_owners_phonenumber = phonenumbers.format_number(owners_phonenumber, phonenumbers.PhoneNumberFormat.E164)
            flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_normalised_owners_phonenumber'),
    ]

    operations = [
        migrations.RunPython(normalize_owners_phone_number),
    ]