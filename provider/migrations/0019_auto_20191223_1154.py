# Generated by Django 2.2.6 on 2019-12-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0018_auto_20191126_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='vcseprovider',
            name='default_domain',
            field=models.CharField(blank=True, max_length=100, verbose_name='Standarddomän för videoadresser'),
        ),
    ]