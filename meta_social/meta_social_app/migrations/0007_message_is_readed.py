# Generated by Django 3.0.5 on 2020-05-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta_social_app', '0006_auto_20200513_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_readed',
            field=models.BooleanField(default=False),
        ),
    ]
