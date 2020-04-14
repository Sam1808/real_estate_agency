# Generated by Django 2.2.4 on 2020-04-04 20:37

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20200403_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='flat_owners',
            field=models.ManyToManyField(to='property.Owner', verbose_name='Собственики квартиры', related_name='owner_flats'),
        ),
    ]
