# Generated by Django 2.2.19 on 2021-05-24 12:35

from django.db import migrations, models


def set_active(apps, schema_editor):

    F = models.F

    Meeting = apps.get_model('meeting', 'Meeting')
    Meeting.objects.filter(ts_activated=None, backend_active=True).update(ts_activated=F('ts_created'))
    Meeting.objects.filter(ts_activated=None).exclude(provider_ref2='').update(ts_activated=F('ts_created'))


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('meeting', '0003_auto_20210510_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='ts_activated',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.RunPython(set_active, migrations.RunPython.noop),
    ]