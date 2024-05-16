
from django import forms
from .models import Habit, Goal, StudyDay, CategoryHabit


class HabitForm(forms.ModelForm):
    class Meta:
        model = CategoryHabit
        fields = ['name']


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['goal', 'category', 'month']


class StudyDayForm(forms.ModelForm):
    class Meta:
        model = StudyDay
        fields = ['study_time', 'category']
