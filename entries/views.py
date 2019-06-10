from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView 
from django.forms import ModelForm, formset_factory
from entries.models import Fixtures, Question, Players, entry_data
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from dal import autocomplete
from entries.forms import entryform

class PlayerAutocomplete(autocomplete.Select2QuerySetView):
    def get_result_label(self, item):
        return item.player_name
    def get_queryset(self):
        #if not self.request.user.is_authenticated():
          #  return Players.objects.none()
        def __str__(self):
            return self.player_name
        qs = Players.objects.all()

        if self.q:
            qs = qs.filter(player_name__contains=self.q)

        return qs

    

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
    #u = User.objects.get(username=u)
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

class entryview(TemplateView):
    template_name = 'entries/entries_form_df.html'
    #goalrange = range(10)
    #totalgoals = range(50)
    #fixtures = Fixtures.objects.all()
    #questions = Question.objects.all()

    
    def get(self, request):
        #game_week = Fixtures.objects.filter(game_week='1')
        form = entryform()
        #ffs = formset_factory(entryform)
        #formset = ffs
        #form = ggwf
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = entryform(request.POST) 
        if form.is_valid():
            text = form.cleaned_data['post']
            context = {
            'fixtures': fixtures,
            'questions': questions,
            'goalrange': goalrange,
            'totalgoals': totalgoals,
            'form': form
            }
        return render(request, self.template_name, context)

    
   