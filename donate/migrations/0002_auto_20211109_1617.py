# Generated by Django 2.2 on 2021-11-09 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='user_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Profile'),
        ),
    ]
