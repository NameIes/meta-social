# Generated by Django 3.0.6 on 2020-05-27 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_auto_20200520_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='country',
        ),
    ]