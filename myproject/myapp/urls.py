from django.urls import path
from .views import create_account
#myapp\urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# myapp\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',  views.movie_list, name='home'),  # Главная страница
    path('authorization', views.create_account, name='authorization'),
    path('login/', views.authorization3, name='login'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('logout/', views.user_logout, name='logout'),
    path('movies/<int:movie_id>/', views.movie_details, name='movie_details'),
    # URL для выхода из системы
    # Страница авторизации
    # Другие URL-маршруты вашего приложения
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


