# Generated by Django 3.0.6 on 2020-05-29 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message_music'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='is_readed',
            new_name='is_read',
        ),
    ]