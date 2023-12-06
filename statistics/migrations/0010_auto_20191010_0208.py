# Generated by Django 2.1.5 on 2019-10-10 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0009_auto_20191010_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='leg',
            name='target_fk',
            field=models.ForeignKey(db_index=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='statistics.Target'),
        ),
        migrations.AlterField(
            model_name='leg',
            name='ou_fk',
            field=models.ForeignKey(db_index=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='statistics.Ou'),
        ),
        migrations.AlterField(
            model_name='leg',
            name='tenant_fk',
            field=models.ForeignKey(db_index=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='statistics.Tenant'),
        ),
    ]