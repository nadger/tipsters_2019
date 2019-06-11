from django import forms
from django.forms import ModelForm, formset_factory
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Fixtures, Players, entry_data, configdata
from crispy_forms.helper import FormHelper
from dal import autocomplete

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'comments')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'comments')

class gwadmin(forms.ModelForm):
	class Meta:
		model = configdata
		fields = ('gameweek', 'season', 'gw_deadline', 'gw_active', 'gw_closed')
		widgets = {
            'gw_deadline': forms.widgets.DateTimeInput(),
        }
		

class entryform(forms.Form):
	score_h1_f1 = forms.DecimalField(min_value=0,max_value=20,max_digits=2,decimal_places=0,initial=0,required=True)
	score_a1_f1 = forms.DecimalField(min_value=0,max_value=20,max_digits=2,decimal_places=0,initial=0,required=True)
	totalgoals = forms.DecimalField(min_value=0,max_value=99,max_digits=2,decimal_places=0,initial=0,required=True)
	player_4 = forms.ModelChoiceField(
		queryset=Players.objects.all(),
        widget=autocomplete.ModelSelect2(url='player-autocomplete')
    )
	player_3 = forms.ModelChoiceField(
		queryset=Players.objects.all(),
        widget=autocomplete.ModelSelect2(url='player-autocomplete')
    )
	player_2 = forms.ModelChoiceField(
		queryset=Players.objects.all(),
        widget=autocomplete.ModelSelect2(url='player-autocomplete')
    )
	player_1 = forms.ModelChoiceField(
		queryset=Players.objects.all(),
        widget=autocomplete.ModelSelect2(url='player-autocomplete')
    )
	#class Meta:
	#	model = entry_data
	#	fields = ('__all__')
 


