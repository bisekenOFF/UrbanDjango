from django.shortcuts import render
from django.views import View


def func(request):
    return render(request, 'second_task/func.html')


class ClassView(View):
    def get(self, request):
        return render(request, 'second_task/class.html')
