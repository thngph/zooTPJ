# Generated by Django 2.2 on 2021-11-20 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0003_auto_20211119_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_ID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=1000)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
            ],
        ),
    ]
