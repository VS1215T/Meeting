# Generated by Django 2.2.6 on 2021-01-22 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0051_auto_20210121_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='ts_unbooked',
            field=models.DateTimeField(null=True, editable=False),
        ),
    ]