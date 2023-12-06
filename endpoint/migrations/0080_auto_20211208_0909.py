# Generated by Django 2.2.24 on 2021-12-08 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('endpoint', '0079_auto_20211207_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='customersettings',
            name='default_portal_address_book',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to='address.AddressBook',
            ),
        ),
    ]