from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import *


# Create your views here.

def menu(request):
    title = 'Главная страница'
    text = "Главная страница"
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'menu.html', context)


def Shop(request):
    title = 'Магазин'
    text = "Магазин"
    list_game = Game.objects.all()
    context = {
        'title': title,
        'text': text,
        'list_game': list_game,
    }
    return render(request, 'Shop.html', context)


def Basket(request):
    title = 'Корзина'
    text = "Корзина"
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'Basket.html', context)


def registration_page_django(request):
    users = []
    Buyers = Buyer.objects.all()
    for user in Buyers:
        users.append(user.name)

    info = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page_django.html', info)
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page_django.html', info)
            elif username in users:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page_django.html', info)
            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = ContactForm()

    info['form'] = form
    return render(request, 'registration_page_django.html', {'info': info})
