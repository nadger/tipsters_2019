from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm, formset_factory, modelformset_factory, inlineformset_factory
from entries.models import Fixtures, Question, Players, entry_data_new, configdata, usr_teams
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from dal import autocomplete
from entries.forms import entryform, gwadmin, score_entry, totalgoals_form

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
    active_gw = configdata.objects.filter(gw_active=1)
    team_name = "xxx"
    context = {
        'team_name': team_name,
        'active_gw': active_gw
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
def error(request):
    context = {
        'error': error,
    }

    return render(request, 'entries/error.html', context)

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
    def get(self, request, pk):
        #game_week = Fixtures.objects.filter(game_week='1')
        current_user = request.user
        current_usrid = current_user.id
        current_gw = pk
        gwdata = get_object_or_404(configdata, id = current_gw)
        if gwdata.gw_active == False:
            return render(request, 'entries/error.html')
        gw_fix = Fixtures.objects.filter(game_week__pk = current_gw)
        if entry_data_new.objects.filter(team_id__pk = current_usrid, entry_gw = pk).exists():
            entry_data = entry_data_new.objects.get(team_id__pk = current_usrid, entry_gw = pk)
            EntryFormSet = score_entry(instance = entry_data)
        else:
                EntryFormSet = score_entry(initial={
                    'fixture_id1': gw_fix[0].pk,
                    'fixture_id2': gw_fix[1].pk,
                    'fixture_id3': gw_fix[2].pk,
                    'fixture_id4': gw_fix[3].pk,
                    'fixture_id5': gw_fix[4].pk,
                    'fixture_id6': gw_fix[5].pk,
                    'fixture_id7': gw_fix[6].pk,
                    'fixture_id8': gw_fix[7].pk,
                    'fixture_id9': gw_fix[8].pk,
                    'fixture_id10': gw_fix[9].pk,
                    'entry_gw': current_gw,
                    'team_id' : current_usrid,
                    })
        form = EntryFormSet
        context = {
            'gw_fix': gw_fix,
            'form': form
            }
        return render(request, self.template_name, {'context': context})

    def post(self, request, pk):
        current_user = request.user
        current_usrid = current_user.id
        gw_fix = Fixtures.objects.filter(game_week = pk)
        if entry_data_new.objects.filter(team_id__pk = current_usrid, entry_gw = pk).exists():
            update_ins = entry_data_new.objects.get(team_id__pk = current_usrid, entry_gw = pk)
            form = score_entry(request.POST, instance = update_ins)
        else:
            form = score_entry(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.entry_GW = pk
            post.entry_team = current_usrid
            post.save()
        context = {
            'gw_fix': gw_fix,
            'form': form
            }
        return render(request, self.template_name, {'context': context})



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
