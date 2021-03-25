# Generated by Django 3.0.6 on 2021-03-24 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gdstorage.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('custom_name', models.CharField(blank=True, max_length=50, null=True)),
                ('time_ran', models.DateTimeField(auto_now_add=True, null=True)),
                ('input_image', models.ImageField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='input_image')),
                ('method', models.IntegerField()),
                ('successful', models.BooleanField(default=False)),
                ('submitting_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HarrisCorners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_image', models.ImageField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='HarrisCorners/output_image')),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Run')),
            ],
        ),
    ]
