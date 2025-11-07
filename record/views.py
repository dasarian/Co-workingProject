# record/views.py

from django.shortcuts import render

def record_main_page(request):
    """
    Эта функция обрабатывает запрос и возвращает наш шаблон.
    """
    return render(request, 'record/index.html')