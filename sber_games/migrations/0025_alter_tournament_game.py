# Generated by Django 3.2.9 on 2021-11-18 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sber_games', '0024_auto_20211118_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='game',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sber_games.game'),
        ),
    ]
