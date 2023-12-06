# Generated by Django 2.2.12 on 2020-06-26 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roomcontrol', '0008_auto_20200626_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='EndpointControlState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('controls', models.ManyToManyField(to='roomcontrol.RoomControl')),
                ('endpoint', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='endpoint.Endpoint')),
                ('templates', models.ManyToManyField(to='roomcontrol.RoomControlTemplate')),
            ],
        ),
    ]