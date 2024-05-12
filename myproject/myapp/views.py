from django.shortcuts import render
from django.utils import timezone

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from .forms import MovieForm
from .forms import LoginForm
from .models import User
from .models import Movie1

def add_movie(request):
    if request.user.role != 'admin':
        return redirect('home')  # Предположим, что у вас есть представление 'home'

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('home')  # Предположим, что у вас есть представление 'home'
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})


def movie_list(request):
    movies = Movie1.objects.all()
    return render(request, 'home.html', {'movies': movies})

def my_view(request):
    if request.user.is_authenticated:
        if request.user.role == 'admin':
            # Действия для администратора
            return render(request, 'admin_page.html')
        else:
            # Действия для обычного пользователя
            return render(request, 'normal_user_page.html')
    else:
        # Если пользователь не аутентифицирован, перенаправляем его на страницу входа
        return redirect('login.html')

def create_account(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Начало сессии для пользователя
            login(request, user)
            return redirect('home')  # Перенаправление на домашнюю страницу
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def add_movie(request):
    return render(request, 'add_movie.html')
from django.contrib.auth import get_user_model

def authorization3(request):
    message = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Фильтрация пользователей по email и паролю
        users = User.objects.filter(email=email, password=password)
        if users.exists():
            # Получение первого пользователя из отфильтрованного списка
            user = users.first()
            # Логин пользователя
            login(request, user)
            # Ваша логика с сеансами
            # Например, обновление даты последнего входа
            user.last_login = timezone.now()
            user.save(update_fields=['last_login'])

            if user.is_superuser:
                # Если пользователь администратор, перенаправляем на страницу администратора
                return redirect('admin:index')
            else:
                # Если пользователь не администратор, перенаправляем на другую страницу
                return redirect('home')  # Измените 'home' на URL вашей целевой страницы
        else:
            message = 'Invalid email or password.'
    return render(request, 'authorization.html', {'message': message})


def user_logout(request):
    logout(request)
    return redirect('home')  # Перенаправление на главную страницу или любую другую страницу
