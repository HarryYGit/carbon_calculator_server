from django.urls import path
from tasks_carbon import views

urlpatterns = [
    path('tasks/', views.tasks_carbon),
]