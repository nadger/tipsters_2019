# Generated by Django 2.2.1 on 2019-06-05 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_results_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_teamname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
