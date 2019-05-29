from django.contrib import admin

# Register your models here.
from .models import Fixtures, Teams, Question, Players

admin.site.register(Fixtures)
admin.site.register(Teams)
admin.site.register(Question)
admin.site.register(Players)