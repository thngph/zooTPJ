# Generated by Django 2.2 on 2021-11-13 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_auto_20211113_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='expired',
            field=models.DateTimeField(blank=True),
        ),
    ]
