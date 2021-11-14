# Generated by Django 3.2.9 on 2021-11-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_profiles', '0003_delete_register_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='register_USER',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(db_index=True, max_length=255)),
                ('password', models.CharField(default=None, max_length=255)),
                ('first_name', models.CharField(default=None, max_length=255)),
                ('second_name', models.CharField(default=None, max_length=255)),
                ('last_name', models.CharField(default=None, max_length=255)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('tab_number', models.CharField(max_length=255)),
                ('game_account', models.CharField(max_length=255)),
                ('game', models.CharField(max_length=255)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'register_USER',
            },
        ),
    ]
