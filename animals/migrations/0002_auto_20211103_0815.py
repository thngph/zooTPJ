# Generated by Django 2.2 on 2021-11-03 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='profile_img',
            field=models.FilePathField(default=''),
        ),
        migrations.AlterField(
            model_name='animal',
            name='img',
            field=models.FilePathField(default=''),
        ),
    ]
