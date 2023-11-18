from django.test import TestCase
from datetime import timedelta
from .models import Task, RepetitionPattern

class RepetitionPatternModelTest(TestCase):
    def test_calculate_next_due_date_daily(self):
        pattern = RepetitionPattern.objects.create(frequency='day(s)', day_interval=2)
        current_due_date = timedelta(days=3)
        next_due_date = pattern.calculate_next_due_date(current_due_date)
        self.assertEqual(next_due_date, current_due_date + timedelta(days=2))

    def test_calculate_next_due_date_weekly(self):
        pattern = RepetitionPattern.objects.create(frequency='week(s)', week_interval=2)
        current_due_date = timedelta(weeks=3)
        next_due_date = pattern.calculate_next_due_date(current_due_date)
        self.assertEqual(next_due_date, current_due_date + timedelta(weeks=2))


class TaskModelTest(TestCase):
    def setUp(self):
        self.pattern = RepetitionPattern.objects.create(frequency='day(s)', day_interval=1)
        self.task = Task.objects.create(
            name="Test Task",
            status="to-do",
            due_date=timedelta(days=1),
            description="Test Description",
            category="Test Category",
            repetition=self.pattern
        )



class TaskViewsTest(TestCase):
    def setUp(self):
        self.pattern = RepetitionPattern.objects.create(frequency='day(s)', day_interval=1)
        self.task = Task.objects.create(
            name="Test Task",
            status="to-do",
            due_date=timedelta(days=1),
            description="Test Description",
            category="Test Category",
            repetition=self.pattern
        )
