# Generated by Django 4.2.7 on 2023-12-04 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0003_alter_advertisement_status'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='favourites',
            constraint=models.UniqueConstraint(fields=('user', 'advertisement'), name='user_adv_combination'),
        ),
    ]