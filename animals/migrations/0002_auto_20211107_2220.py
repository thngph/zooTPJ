# Generated by Django 2.2 on 2021-11-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='img',
            field=models.FileField(default='', upload_to='photos/animals'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='profile_img',
            field=models.FileField(default='', upload_to='photos/animals'),
        ),
    ]
