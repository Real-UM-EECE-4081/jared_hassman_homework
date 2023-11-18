from django.db import models
from datetime import timedelta


class Task(models.Model):
    STATUS_CHOICES = [
        ('to-do', 'To Do'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    def get_next_due_date(self):
        if self.repetition:
            return self.repetition.calculate_next_due_date(self.due_date)
        else:
            return None

    name = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True)
    completion_time = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True)
    repetition = models.ForeignKey('RepetitionPattern', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

class RepetitionPattern(models.Model):
    FREQUENCY_CHOICES = [
        ('day(s)', 'Day(s)'),
        ('week(s)', 'Week(s)'),
        ('month(s)', 'Month(s)'),
    ]

    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    day_interval = models.IntegerField(default=1)
    week_interval = models.IntegerField(default=1)
    month_interval = models.IntegerField(default = 1)

    def calculate_next_due_date(self, current_due_date):
        if self.frequency == 'day(s)':
            return current_due_date + timedelta(days=self.day_interval)
        elif self.frequency == 'week(s)':
            return current_due_date + timedelta(weeks=self.week_interval)
        elif self.frequency == 'month(s)':
            return current_due_date + timedelta(months=self.month_interval)

        return None


    def __str__(self):
        if self.frequency == 'day(s)':
            if self.day_interval == 1:
                return f"Every Day"
            else:
                return f"Daily - every {self.day_interval} days"
        if self.frequency == 'week(s)':
            if self.week_interval == 1:
                return f"Every Week"
            else:
                return f"Weekly - every {self.week_interval} weeks"
        if self.frequency == 'month(s)':
            if self.month_interval == 1:
                return f"Every Month"
            else:
                return f"Monthly - every {self.month_interval} months"
