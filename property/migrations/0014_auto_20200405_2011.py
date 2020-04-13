# Generated by Django 2.2.4 on 2020-04-05 17:11

from django.db import migrations
from django.apps import apps

def connect_owners_and_flats(apps, schema_editor):
    flats = apps.get_model('property', 'Flat')
    owners = apps.get_model('property', 'Owner')

    for flat in flats.objects.all():
        owner, other_data = owners.objects.get_or_create(
            owner = flat.owner,
            owners_phonenumber = flat.owners_phonenumber,
            normalised_owners_phonenumber = flat.normalised_owners_phonenumber,
        )
        owner.own_flats.add(flat)
        owner.save()
        flat.flat_owners.add(owner)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20200405_1906'),
    ]

    operations = [
        migrations.RunPython(connect_owners_and_flats)
    ]