from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Fixtures, Teams, Question, Players, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

admin.site.register(Fixtures)
admin.site.register(Teams)
admin.site.register(Question)
admin.site.register(Players)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)