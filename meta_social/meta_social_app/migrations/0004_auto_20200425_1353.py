# Generated by Django 3.0.5 on 2020-04-25 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meta_social_app', '0003_auto_20200425_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimages',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='10+', to=settings.AUTH_USER_MODEL),
        ),
    ]
