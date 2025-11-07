from django.shortcuts import render

def show_task_page(request):
    task = {
        'title': 'Разработать главную страницу',
        'date_posted': '2023-10-27',
        'deadline': '2023-11-10',
        'description': 'Создать адаптивный HTML-макет и стили для главной страницы коворкинга с использованием Flexbox. Убедиться, что страница корректно отображается на мобильных устройствах.',
        'assignee': 'Иванов Иван'
    }

    context = {
        'task': task
    }

    return render(request, 'mainpage/task_detail.html', context)