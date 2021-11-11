# Generated by Django 3.2.9 on 2021-11-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GAMES',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('fio', models.CharField(max_length=255)),
                ('tab_number', models.CharField(max_length=255)),
                ('game_account', models.CharField(max_length=255)),
                ('game', models.CharField(max_length=255)),
            ],
        ),
    ]
