from django import forms
from sber_games.models import TOURNAMENT, GAME


class TournamentForm(forms.ModelForm):
    class Meta:
        model = TOURNAMENT
        fields = '__all__'
        exclude = ['status']


class GameForm(forms.ModelForm):
    class Meta:
        model = GAME
        fields = '__all__'
        exclude = ['status']
