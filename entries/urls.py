from django.urls import path, re_path
from entries.views import PlayerAutocomplete
from . import views


urlpatterns = [
    path('entry', views.index, name='index'),
    path('entry2', views.entryview.as_view(), name='entry2'),
    path('login', views.login, name='login'),
    path('menu', views.menu, name='menu'),
    path('league', views.league, name='league'),
    path('gwresult', views.gwresult, name='league'),
    re_path(r'^player-autocomplete/$', PlayerAutocomplete.as_view(), name='player-autocomplete'),

]
