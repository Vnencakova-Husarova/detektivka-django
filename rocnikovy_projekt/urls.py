from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('admin/', admin.site.urls),
    path('game/', views.game_page, name='game'),
]
