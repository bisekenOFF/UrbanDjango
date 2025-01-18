from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


# Create your views here.
users = ["user", "admin", "bisekenov"]

def registration_page(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'fifth_task/registration_page.html', info)
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return render(request, 'fifth_task/registration_page.html', info)
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            return render(request, 'fifth_task/registration_page.html', info)
        else:
            users.append(username)
            return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'fifth_task/registration_page.html', {'info': info})


def registration_page_django(request):
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
                return render(request, 'fifth_task/registration_page_django.html', info)
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'fifth_task/registration_page_django.html', info)
            elif username in users:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'fifth_task/registration_page_django.html', info)
            else:
                users.append(username)
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = ContactForm()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', {'info': info})
