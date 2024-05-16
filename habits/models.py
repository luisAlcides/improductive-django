
from django.db import models
import datetime


class CategoryHabit(models.Model):
    name = models.CharField(max_length=255)
    date_current = models.DateTimeField(
        default=datetime.datetime.now)  # Proveer un valor por defecto

    def __str__(self):
        return self.name


class Month(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Goal(models.Model):
    goal = models.FloatField()
    category = models.ForeignKey(CategoryHabit, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    date_current = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category.name} - {self.month.name}"


class Habit(models.Model):
    study_time = models.FloatField()
    category = models.ForeignKey(CategoryHabit, on_delete=models.CASCADE)
    date_current = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category.name} - {self.study_time} hours"


class StudyDay(models.Model):
    category = models.ForeignKey(CategoryHabit, on_delete=models.CASCADE)
    study_time = models.FloatField()
    date_current = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category.name} - {self.study_time} hours on {self.date_current}"
