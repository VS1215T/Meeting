# Generated by Django 2.2.23 on 2021-06-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0064_auto_20210510_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='clustersettings',
            name='dial_out_location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='clustersettings',
            name='theme_profile',
            field=models.CharField(max_length=200, null=True),
        ),
    ]