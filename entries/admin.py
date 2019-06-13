from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Fixtures, Teams, Question, Players, CustomUser, usr_teams, configdata, Answer, entry_data, Total_Goal_Entry, entry_q_answers, entry_scorers
from .forms import CustomUserCreationForm, CustomUserChangeForm

admin.site.register(Fixtures)
admin.site.register(Teams)
admin.site.register(Question)
admin.site.register(Players)
admin.site.register(usr_teams)
admin.site.register(configdata)
admin.site.register(Answer)
admin.site.register(entry_data)
admin.site.register(Total_Goal_Entry)
admin.site.register(entry_q_answers) 
admin.site.register(entry_scorers)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']

admin.site.register(CustomUser, CustomUserAdmin)