# Generated by Django 5.0.3 on 2024-03-29 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveyapp', '0003_remove_questions_q_id_remove_response_r_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question_types',
            name='text',
        ),
        migrations.AddField(
            model_name='questions',
            name='q_options',
            field=models.JSONField(null=True),
        ),
    ]