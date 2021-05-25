# Generated by Django 3.2.3 on 2021-05-23 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdetails',
            name='Location',
            field=models.CharField(default='college', max_length=20),
        ),
        migrations.AddField(
            model_name='user_details',
            name='registeredevent',
            field=models.ImageField(default='image', upload_to='pics'),
            preserve_default=False,
        ),
    ]
