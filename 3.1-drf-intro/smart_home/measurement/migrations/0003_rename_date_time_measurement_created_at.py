# Generated by Django 4.2.7 on 2023-11-09 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_rename_sensor_id_measurement_sensor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='date_time',
            new_name='created_at',
        ),
    ]