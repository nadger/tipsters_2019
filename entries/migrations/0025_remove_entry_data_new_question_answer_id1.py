# Generated by Django 3.2.7 on 2021-10-05 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0024_alter_entry_data_new_question_answer_id1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry_data_new',
            name='question_answer_id1',
        ),
    ]
