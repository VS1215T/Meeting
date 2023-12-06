# Generated by Django 2.2.6 on 2020-01-23 17:05

from django.db import migrations, models


def backward(apps, schema_editor):
    move_data(apps, schema_editor, reverse=True)


def move_data(apps, schema_editor, reverse=False):
    # NOTE: wont work with auto_now_add or many2manyfields

    from django.core.management.color import no_style
    from django.db import DEFAULT_DB_ALIAS, connections

    connection = connections[DEFAULT_DB_ALIAS]
    for m in ('EndpointTask', 'EndpointFirmware', 'EndpointTemplate'):
        Model = apps.get_model('endpoint', m)
        Model2 = apps.get_model('endpoint_provision', m)

        if reverse:
            Model, Model2 = Model2, Model

        for m in Model2.objects.raw('SELECT * FROM {}'.format(Model._meta.db_table)):
            m.save(force_insert=True)

        statements = connection.ops.sequence_reset_sql(no_style(), [Model2])
        schema_editor.connection.cursor().execute('\n'.join(statements))



class Migration(migrations.Migration):

    dependencies = [
        ('endpoint', '0041_auto_20200123_1503'),
        ('endpoint_provision', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(move_data, reverse_code=backward),
        migrations.RemoveField(
            model_name='endpointtask',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='endpointtask',
            name='endpoint',
        ),
        migrations.RemoveField(
            model_name='endpointtemplate',
            name='customer',
        ),
        migrations.AlterField(
            model_name='endpointdatacontent',
            name='content_type',
            field=models.SmallIntegerField(choices=[(0, 'configuration'), (1, 'status'), (2, 'command'), (10, 'macros'), (11, 'panels')]),
        ),
        migrations.DeleteModel(
            name='EndpointFirmware',
        ),
        migrations.DeleteModel(
            name='EndpointTask',
        ),
        migrations.DeleteModel(
            name='EndpointTemplate',
        ),
    ]