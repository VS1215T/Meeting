# Generated by Django 2.2.24 on 2021-10-13 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0004_meeting_ts_activated'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='ts_deprovisioned',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='ts_provisioned',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]