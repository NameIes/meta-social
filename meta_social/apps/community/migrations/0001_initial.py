# Generated by Django 3.0.5 on 2020-05-14 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('info', models.CharField(max_length=1000, null=True)),
                ('base_image', models.ImageField(default='avatars/users/0.png', upload_to='avatars/communities')),
                ('image', models.ImageField(default='avatars/users/0.png', upload_to='avatars/communities')),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('admins', models.ManyToManyField(related_name='admins', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]