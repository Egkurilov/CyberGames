from django import forms
from sber_games.models import TOURNAMENT


class TournamentForm(forms.ModelForm):
    class Meta:
        model = TOURNAMENT
        fields = '__all__'
        exclude = ['status']
