# Generated by Django 3.0.5 on 2020-04-24 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meta_social_app', '0005_auto_20200424_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='administrators',
            field=models.ManyToManyField(null=True, related_name='chat_administrators', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
