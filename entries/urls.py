from django.urls import path, re_path
from django.contrib.auth.decorators import login_required, permission_required
from entries.views import PlayerAutocomplete
from . import views


urlpatterns = [
    path('entry', views.index, name='index'),
    path('entry2', login_required(views.entryview.as_view()), name='entry2'),
    path('entry/<int:pk>', login_required(views.entryview.as_view()), name='entry'),
    path('login', views.login, name='login'),
    path('menu', views.menu, name='menu'),
    path('error', views.menu, name='error'),
    path('admin', views.admin, name='admin'),
    path('league', views.league, name='league'),
    path('gwresult', views.gwresult, name='league'),
    path('logout', views.logout_view, name='logout'),
    path('admin/gwview', views.GWList.as_view(), name='GW_list'),
    path('admin/gwdetail/<int:pk>', views.GWDetail.as_view(), name='GW_detail'),
    path('admin/gw_create', views.GWCreate.as_view(), name='GW_create'),
    path('admin/gw_update/<int:pk>', views.GWUpdate.as_view(), name='GW_update'),
    path('admin/gw_delete/<int:pk>', views.GWDelete.as_view(), name='GW_delete'),
    re_path(r'^player-autocomplete/$', login_required(PlayerAutocomplete.as_view()), name='player-autocomplete'),

]
