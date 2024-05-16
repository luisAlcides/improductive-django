
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_goal/', views.add_goal, name='add_goal'),
    path('add_habit/', views.add_habit, name='add_habit'),
    path('add_study_day/', views.add_study_day, name='add_study_day'),
    path('delete_goal/<int:goal_id>/', views.delete_goal, name='delete_goal'),
    path('update_goal/<int:goal_id>/', views.update_goal, name='update_goal'),
]
