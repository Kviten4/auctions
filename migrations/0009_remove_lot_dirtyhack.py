# Generated by Django 4.0.5 on 2022-08-03 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_lot_dirtyhack'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lot',
            name='dirtyHack',
        ),
    ]
