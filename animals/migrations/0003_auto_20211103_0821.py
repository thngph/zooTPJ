# Generated by Django 2.2 on 2021-11-03 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_auto_20211103_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='img',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='animal',
            name='profile_img',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
