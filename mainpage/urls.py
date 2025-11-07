from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage_main_page, name='mainpage_main_page'),
    path('task/', views.show_task_page, name='task_detail'),
]