from django import forms
from .models import Task, RepetitionPattern

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'status', 'due_date', 'description', 'completion_time', 'repetition', 'category']

    repetition = forms.ModelChoiceField(
        queryset=RepetitionPattern.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label = 'Repetition Pattern'
    )
