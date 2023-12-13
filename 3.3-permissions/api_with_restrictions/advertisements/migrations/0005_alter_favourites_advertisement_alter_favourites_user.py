# Generated by Django 4.2.7 on 2023-12-04 22:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisements', '0004_favourites_user_adv_combination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourites',
            name='advertisement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='favourites', to='advertisements.advertisement'),
        ),
        migrations.AlterField(
            model_name='favourites',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]