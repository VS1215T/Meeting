# Generated by Django 2.1.5 on 2019-09-12 07:39

import django.db.models.deletion
from django.db import migrations, models


def set_customer(apps, schema):

    EndpointTask = apps.get_model('endpoint.EndpointTask')
    for t in EndpointTask.objects.all():
        if t.endpoint_id and not t.customer_id:
            t.customer_id = t.endpoint.customer
            t.save()

    EndpointTask.objects.filter(customer__isnull=True).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0017_merge_20190903_0934'),
        ('endpoint', '0029_endpoint_connection_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpointtask',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='provider.Customer'),
        ),
        migrations.RunPython(set_customer, lambda *args, **kwargs: True),
    ]