# Generated by Django 2.2.6 on 2020-10-11 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoint', '0054_auto_20200612_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoint',
            name='api_port',
            field=models.SmallIntegerField(blank=True, default=443, null=True),
        ),
    ]