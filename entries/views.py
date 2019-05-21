from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from entries.models import Fixtures

def login(request):
	return render(request, 'entries/login.html')


def index(request):
    fixtures = Fixtures.objects.all()
    context = {
        'fixtures': fixtures
    }
    return render(request, 'entries/entries_form.html', context)