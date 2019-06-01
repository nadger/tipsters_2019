from django.contrib import admin

# Register your models here.
from .models import Fixtures, Teams, Question, Players, User_details

admin.site.register(Fixtures)
admin.site.register(Teams)
admin.site.register(Question)
admin.site.register(Players)
admin.site.register(User_details)
