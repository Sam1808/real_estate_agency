# Generated by Django 2.2.4 on 2020-03-25 20:19

from django.db import migrations
from django.apps import apps

def determine_new_building(apps, schema_editor):
    flats = apps.get_model('property', 'Flat')
    for flat in flats.objects.all():
        if flat.construction_year >= 2015:
            flat.new_building = True
        else:
            flat.new_building = False
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20200325_2302'),
    ]

    operations = [
        migrations.RunPython(determine_new_building)
    ]
