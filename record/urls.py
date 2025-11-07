from django.urls import path
from . import views

urlpatterns = [
    # Пустой путь '' означает, что это будет главная страница приложения
    path('', views.record_main_page, name='record_main_page'),
]