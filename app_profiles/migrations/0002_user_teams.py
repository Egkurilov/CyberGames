# Generated by Django 3.2.9 on 2021-11-18 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sber_games', '0024_auto_20211118_2005'),
        ('app_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='teams',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='sber_games.team'),
        ),
    ]
