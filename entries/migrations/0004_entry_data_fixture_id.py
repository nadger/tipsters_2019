# Generated by Django 2.2.1 on 2019-06-10 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_customuser_user_teamname'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry_data',
            name='fixture_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='entries.Fixtures'),
        ),
    ]