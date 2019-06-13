from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm, formset_factory, modelformset_factory, inlineformset_factory
from entries.models import Fixtures, Question, Players, entry_data, configdata
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from dal import autocomplete
from entries.forms import entryform, gwadmin, score_entry

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

    
@login_required
def menu(request):
    #u = User.objects.get(username=u)
    team_name = "xxx"
    context = {
        'team_name': team_name,
    }

    return render(request, 'entries/menu.html', context)

@login_required
def admin(request):
    team_name = "xxx"
    context = {
        'team_name': team_name,
    }

    return render(request, 'entries/admin.html', context)

@login_required
def league(request):
	return render(request, 'entries/menu.html')

@login_required
def gwresult(request):
	return render(request, 'entries/results.html')     

@login_required
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
    
    #questions = Question.objects.all()
    
    
    def get(self, request):
        #game_week = Fixtures.objects.filter(game_week='1')
        fixtures = Fixtures.objects.get(game_week__gameweek='1')
        #fixtures = Fixtures.objects.all()
        FixtureFormSet = inlineformset_factory(Fixtures, entry_data, form = score_entry)
        formset = FixtureFormSet(instance = fixtures)
        #form = score_entry()
        #ffs = formset_factory(entryform)
        #formset = ffs
        #form = ggwf
        context = {
            'fixtures': fixtures,
            'formset': formset
            }
        return render(request, self.template_name, {'formset': formset})

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


def logout_view(request):
    logout(request)
    # Redirect to a success page.


class GWList(ListView):
    model = configdata  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 

class GWDetail(DetailView):
    model = configdata  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 

class GWCreate(CreateView):
    model = configdata  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 

class GWUpdate(UpdateView):
    model = configdata  
    form_class = gwadmin
    #fields = ['gameweek', 'season', 'gw_deadline', 'gw_active', 'gw_closed']
    success_url = '/entries/admin/gwview'
    

class GWDelete(DeleteView):
    model = configdata  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 