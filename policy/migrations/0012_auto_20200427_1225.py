# Generated by Django 2.2.6 on 2020-04-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0011_auto_20200424_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activeparticipant',
            name='guid',
            field=models.CharField(max_length=500),
        ),
    ]