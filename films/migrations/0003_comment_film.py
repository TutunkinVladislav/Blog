# Generated by Django 3.2.10 on 2023-08-11 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_alter_post_play'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='film',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='films.post', verbose_name='Фильм'),
        ),
    ]
