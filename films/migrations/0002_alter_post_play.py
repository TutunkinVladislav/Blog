# Generated by Django 3.2.10 on 2023-08-11 18:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='play',
            field=models.IntegerField(help_text='В минутах', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(210)], verbose_name='Продолжительность'),
        ),
    ]
