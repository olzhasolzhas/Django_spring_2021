from django.urls import path, re_path
from .views import todo_list, completed

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('completed', completed, name='completed')
]