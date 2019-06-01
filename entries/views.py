from django.shortcuts import render
from django.http import HttpResponse
from entries.models import Fixtures, Question
from django.contrib.auth import authenticate, login

def loginold(request):
    #username = request.POST['username']
    #password = request.POST['password']
    #user = authenticate(request, username=username, password=password)
    #if user is not None:
    #    login(request, user)
        # Redirect to a success page.
    return render(request, 'entries/login.html')
    #else:
        # Return an 'invalid login' error message.
     #   return render(request, 'entries/menu.html')
    #return render(request, 'entries/login.html')

def menu(request):
    #u = User.objects.get(username=user.username)
    team_name = "xxx"
    context = {
        'team_name': team_name,
    }

    return render(request, 'entries/menu.html', context)

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