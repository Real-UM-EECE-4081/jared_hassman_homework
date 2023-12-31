# Generated by Django 4.2.5 on 2023-11-18 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0005_alter_repetitionpattern_frequency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repetitionpattern',
            old_name='interval',
            new_name='day_interval',
        ),
        migrations.AddField(
            model_name='repetitionpattern',
            name='month_interval',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='repetitionpattern',
            name='week_interval',
            field=models.IntegerField(default=1),
        ),
    ]
