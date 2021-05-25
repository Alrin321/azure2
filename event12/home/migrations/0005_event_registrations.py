# Generated by Django 3.2.3 on 2021-05-25 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_eventdetails_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='event_registrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.eventdetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user_details')),
            ],
        ),
    ]