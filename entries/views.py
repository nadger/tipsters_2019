from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from entries.models import Fixtures, Question

def login(request):
	return render(request, 'entries/login.html')

def menu(request):
	return render(request, 'entries/menu.html')

def league(request):
	return render(request, 'entries/menu.html')

def gwresult(request):
	return render(request, 'entries/results.html')


def index(request):
    goalrange = range(10)
    totalgoals = range(50)
    fixtures = Fixtures.objects.all()
    questions = Question.objects.all()
    context = {
        'fixtures': fixtures,
        'questions': questions,
        'goalrange': goalrange,
        'totalgoals': totalgoals
    }
    
    return render(request, 'entries/entries_form.html', context)