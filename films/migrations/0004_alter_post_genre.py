# Generated by Django 3.2.10 on 2023-08-20 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_comment_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='genre', to='films.genre', verbose_name='Жанр'),
        ),
    ]