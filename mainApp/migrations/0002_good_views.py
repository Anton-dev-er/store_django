# Generated by Django 4.0 on 2022-01-29 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество просмотров'),
        ),
    ]
