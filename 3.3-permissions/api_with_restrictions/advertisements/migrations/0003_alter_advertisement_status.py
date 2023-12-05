# Generated by Django 4.2.7 on 2023-12-01 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_favourites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.TextField(choices=[('OPEN', 'Открыто'), ('CLOSED', 'Закрыто'), ('DRAFT', 'Черновик')], default='OPEN'),
        ),
    ]
