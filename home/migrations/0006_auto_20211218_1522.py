# Generated by Django 2.2 on 2021-12-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20211130_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_valid',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='profile',
            name='key',
            field=models.CharField(default='l-sHGT4FVZR-tNKYASZJzw', max_length=16),
        ),
    ]
