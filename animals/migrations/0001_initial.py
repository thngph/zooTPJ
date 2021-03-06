# Generated by Django 2.2 on 2021-11-05 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('animal_ID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('animal_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('img', models.FileField(default='', upload_to='')),
                ('profile_img', models.FileField(default='', upload_to='')),
            ],
        ),
    ]
