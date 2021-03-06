# Generated by Django 3.0.6 on 2021-03-24 17:11

import chess.apps.users.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, unique=True)),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_service', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('_is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', chess.apps.users.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_service', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=32)),
                ('users', models.ManyToManyField(related_name='unix_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
