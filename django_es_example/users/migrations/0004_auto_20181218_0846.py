# Generated by Django 2.0.9 on 2018-12-18 08:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181218_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='birthday'),
        ),
    ]
