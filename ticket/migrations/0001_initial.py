# Generated by Django 2.2 on 2021-11-05 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticketID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date_purchased', models.DateTimeField(auto_now_add=True)),
                ('ticket_type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Profile')),
            ],
        ),
    ]
