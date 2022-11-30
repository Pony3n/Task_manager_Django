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
    }
    return render(request, 'main/create.html', context)

def registration(request):
    if request.method == 'POST':
        user = UserRegisterForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect('home')
        else:
            error = 'Неправильные данные!'

    user = UserRegisterForm()
    context = {
        'user': user,
    }
    return render(request, 'main/registration.html', context)

def auth(request):
    # if request.method == 'POST':
    #     if user.is_valid():
    #         return redirect('home')
    for user in User.objects.all():
        print(user.email)
    return render(request, 'main/auth.html')
