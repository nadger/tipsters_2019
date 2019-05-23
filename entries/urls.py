from django.urls import path

from . import views

urlpatterns = [
    path('entry', views.index, name='index'),
    path('login', views.login, name='login'),
    path('menu', views.menu, name='menu'),
    path('league', views.league, name='league'),
    path('gwresult', views.gwresult, name='league')


]