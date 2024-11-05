from django.urls import path
from .views import task_list, add_task, mark_as_done, remove_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('mark/<int:task_id>/', mark_as_done, name='mark_as_done'),
    path('remove/<int:task_id>/', remove_task, name='remove_task'),
    path('tasks/<str:status_filter>/', task_list, name='filtered_tasks'),  # Добавили параметр status_filter
]
