# Generated by Django 2.0.9 on 2018-12-18 08:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181218_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 12, 18, 8, 46, 1, 668193, tzinfo=utc), verbose_name='birthday'),
        ),
    ]
