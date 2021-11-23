from django import forms
from sber_games.models import TOURNAMENT, GAME, TEAM


class TournamentForm(forms.ModelForm):
    class Meta:
        model = TOURNAMENT
        fields = '__all__'
        exclude = ['status', 'chat_id', 'created_date']


class GameForm(forms.ModelForm):
    class Meta:
        model = GAME
        fields = '__all__'
        exclude = ['status']


class TeamForm(forms.ModelForm):
    class Meta:
        model = TEAM
        fields = '__all__'
        exclude = ['members', 'status', 'tournament']
