from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'tasks': tasks})


def about_us(request):
    return render(request, 'main/about_us.html')


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно!'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

