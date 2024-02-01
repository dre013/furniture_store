from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том, чем мы занимаемся и почему стоит купить наш товар.',
        }
    return render(request, 'main/about.html', context)
