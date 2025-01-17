from django.shortcuts import render

def main(request):
    title = 'Главная страница'
    text = "Главная страница"
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'third_task/main.html', context)

def Shop(request):
    title = 'Магазин'
    text = "Магазин"
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'third_task/Shop.html', context)

def Basket(request):
    title = 'Корзина'
    text = "Корзина"
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'third_task/Basket.html', context)
