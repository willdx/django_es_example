# Generated by Django 2.0.9 on 2018-12-18 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20181218_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, help_text='Date type: YYYY-MM-DD', null=True, verbose_name='birthday'),
        ),
    ]
