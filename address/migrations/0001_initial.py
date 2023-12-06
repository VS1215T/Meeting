# Generated by Django 2.1.4 on 2018-12-06 13:45

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('provider', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.Customer')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='address.Group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('type', models.SmallIntegerField(choices=[(0, 'Virtual Room'), (10, 'Physical Room'), (20, 'Person')], default=0)),
                ('sip', models.CharField(blank=True, max_length=100, verbose_name='SIP')),
                ('h323', models.CharField(blank=True, max_length=100, verbose_name='H323')),
                ('h323_e164', models.CharField(blank=True, max_length=100, verbose_name='H323 E.164')),
                ('tel', models.CharField(blank=True, max_length=100, verbose_name='Telefon')),
                ('customer', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='provider.Customer')),
                ('group', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.Group')),
            ],
        ),
    ]