# Generated by Django 4.2.5 on 2023-11-17 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completion_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
