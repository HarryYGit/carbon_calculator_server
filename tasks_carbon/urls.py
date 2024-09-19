from django.urls import path
from tasks_carbon import views

urlpatterns = [
    path('tasks/', views.tasks_carbon),
    path('tasks/<int:pk>/',views.tasks_carbon_detail),
]