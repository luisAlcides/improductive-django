
from django.shortcuts import render, redirect, get_object_or_404
from .models import Goal, CategoryHabit, Month, Habit, StudyDay
from .forms import GoalForm, HabitForm, StudyDayForm
from django.db import transaction
import datetime
import matplotlib.pyplot as plt
import io
import urllib
import base64


def index(request):
    current_month = datetime.datetime.now().strftime("%B")
    goals = Goal.objects.filter(month__name=current_month)
    study_days = StudyDay.objects.all()
    chart = generate_chart(study_days, goals)
    context = {
        'goals': goals,
        'study_days': study_days,
        'chart': chart,
    }
    return render(request, 'habits/index.html', context)


def generate_chart(study_days, goals):
    # DPI más alto para mejor calidad
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    ax.set_title("Study Goals and Progress")
    ax.set_xlabel("Goals")
    ax.set_ylabel("Habits")
    legend_labels = ["Goal", 'Habit within Goal',
                     "< 30% Goal", "30%-50% Goal", "> 50% Goal"]
    legend_colors = ["#C0BEBC", '#448BDB', "#FA5F4B", "#F9EC8A", "#73FA8E"]
    goals_name = [goal.category.name for goal in goals]
    goals_value = [goal.goal for goal in goals]

    ax.barh(goals_name, goals_value, color="#C0BEBC",
            edgecolor='black', label="Goals", height=0.5, alpha=0.8)
    study_names = [study.category.name for study in study_days]
    study_values = [study.study_time for study in study_days]
    colors = []

    for study in study_days:
        if study.category.name in goals_name:
            goal = goals.get(category=study.category)
            percentage = (study.study_time / goal.goal) * \
                100 if goal.goal != 0 else 0
            if percentage <= 30:
                colors.append("#FA5F4B")
            elif percentage < 50:
                colors.append("#F9EC8A")
            else:
                colors.append("#73FA8E")
        else:
            colors.append('#448BDB')

    ax.barh(study_names, study_values, color=colors, edgecolor='black',
            label="Studied Hours", height=0.5, alpha=0.8)

    legend_handles = [plt.Rectangle((0, 0), 1, 1, color=color)
                      for color in legend_colors]
    ax.legend(legend_handles, legend_labels, loc="upper right", fontsize=13)

    canvas = plt.gcf().canvas
    buf = io.BytesIO()
    canvas.print_png(buf)
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return uri


def add_goal(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GoalForm()
    return render(request, 'habits/add_goal.html', {'form': form})


def add_habit(request):
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = HabitForm()
    return render(request, 'habits/add_habit.html', {'form': form})


def add_study_day(request):
    if request.method == "POST":
        form = StudyDayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudyDayForm()
    return render(request, 'habits/add_study_day.html', {'form': form})


def delete_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)
    goal.delete()
    return redirect('index')


def update_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)
    if request.method == "POST":
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GoalForm(instance=goal)
    return render(request, 'habits/update_goal.html', {'form': form})
