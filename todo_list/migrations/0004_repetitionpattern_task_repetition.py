# Generated by Django 4.2.5 on 2023-11-18 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_rename_date_completed_task_due_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepetitionPattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], max_length=20)),
                ('interval', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='repetition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='todo_list.repetitionpattern'),
        ),
    ]
