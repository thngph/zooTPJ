# Generated by Django 2.2 on 2021-11-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0004_auto_20211109_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate',
            name='is_expired',
            field=models.BooleanField(default=False),
        ),
    ]
