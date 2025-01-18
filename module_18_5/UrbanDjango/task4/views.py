from django.http import HttpResponse
from django.shortcuts import render


def menu(request):
    title = 'Главная страница'
    text = "Главная страница"
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'fourth_task/menu.html', context)


def Shop(request):
    title = 'Магазин'
    text = "Магазин"
    list_game = {'games': ['Counter Strike 2', 'Player Unknowns Battlegrounds', 'Cyberpunk 2077']}
    context = {
        'title': title,
        'text': text,
        'list_game': list_game,
    }
    return render(request, 'fourth_task/Shop.html', context)


def Basket(request):
    title = 'Корзина'
    text = "Корзина"
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'fourth_task/Basket.html', context)
