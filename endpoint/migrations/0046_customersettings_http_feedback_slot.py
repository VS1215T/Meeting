# Generated by Django 2.2.6 on 2020-02-04 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoint', '0045_auto_20200203_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='customersettings',
            name='http_feedback_slot',
            field=models.SmallIntegerField(default=4, verbose_name='HTTP Feedback Slot'),
        ),
    ]