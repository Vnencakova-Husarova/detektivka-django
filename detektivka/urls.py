from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('game/', views.game_page, name='game'),
]
