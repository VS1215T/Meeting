# Generated by Django 2.2.19 on 2021-03-25 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoint', '0063_auto_20210318_1326'),
        ('meeting', '0001_initial'),
        ('emailbook', '0005_auto_20210325_1653'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=[
            migrations.AlterField(
                model_name='endpoint',
                name='meetings',
                field=models.ManyToManyField(blank=True, related_name='endpoints', through='endpoint.EndpointMeetingParticipant', to='meeting.Meeting'),
            ),
            migrations.AlterField(
                model_name='endpointmeetingparticipant',
                name='meeting',
                field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='meeting.Meeting'),
            ),
        ]),
    ]