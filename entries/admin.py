from django.contrib import admin

# Register your models here.
from .models import Fixtures, Teams, Question

admin.site.register(Fixtures)
admin.site.register(Teams)
admin.site.register(Question)