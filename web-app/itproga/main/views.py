from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['some ', 'hello', '123'],
        'obj': {
            'car': "BMW",
            'age': '18',
            'hobby': 'tennis'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')
