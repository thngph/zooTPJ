# Generated by Django 2.2 on 2021-11-03 02:06

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_auto_20211103_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='img',
            field=models.FileField(default='', storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='animal',
            name='profile_img',
            field=models.FileField(default='', storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to=''),
        ),
    ]
