# Generated by Django 2.2.1 on 2019-05-23 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0005_fixtures_game_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='game_week',
            field=models.PositiveIntegerField(default=0),
        ),
    ]