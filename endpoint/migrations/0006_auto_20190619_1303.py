# Generated by Django 2.1.5 on 2019-06-19 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0014_auto_20190607_1607'),
        ('endpoint', '0005_endpointtemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpointbackup',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='provider.Customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='endpointfirmware',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='provider.Customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='endpointstatus',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='provider.Customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='endpointtemplate',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='provider.Customer'),
            preserve_default=False,
        ),
    ]