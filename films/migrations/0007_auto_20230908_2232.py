# Generated by Django 3.2.10 on 2023-09-08 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(default='', max_length=70, verbose_name='Псевдоним'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=70, verbose_name='Псевдоним'),
        ),
    ]
