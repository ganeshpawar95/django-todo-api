# todo/urls.py
from django.urls import path
from .views import register, login, TodoListCreateView, TodoRetrieveUpdateDestroyView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoRetrieveUpdateDestroyView.as_view(), name='todo-retrieve-update-destroy'),
]
