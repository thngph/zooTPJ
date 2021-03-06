# Generated by Django 2.2 on 2021-11-05 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(default='new user', max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('contact', models.CharField(max_length=15)),
                ('img', models.FileField(default='', upload_to='')),
            ],
        ),
    ]
