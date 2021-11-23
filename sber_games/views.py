from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
# Create your views here.
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from app_profiles.models import USER
from sber_games.forms import TournamentForm, GameForm, TeamForm
from sber_games.models import TOURNAMENT, GAME, TEAM


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'main'
        context['title'] = 'Sber CyberGame'
        context['description'] = 'Sber CyberGame'
        return context


class UserListView(generic.ListView):
    model = USER
    template_name = 'user_list.html'
    context_object_name = 'user_list'
    queryset = USER.objects.all()[:5]


class UserDetailView(generic.DetailView):
    model = USER


def registration(request, *args, **kwargs):
    return render(request, '../app_profiles/templates/profiles/registration.html', {})


def my_game(request, *args, **kwargs):
    return render(request, 'my_game.html', {})


def my_team(request, *args, **kwargs):
    return render(request, 'my_team.html', {})


def user_info(request, *args, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    return render(request, 'user_info.html', {'ip_adress': ip})


class TournamentListView(generic.ListView):
    model = TOURNAMENT
    template_name = 'tournament_list.html'
    context_object_name = 'tournament_list'
    queryset = TOURNAMENT.objects.all()[:100]


class TournamentDetailView(generic.DetailView):
    def get(self, request, *args, **kwargs):
        tournament_view = get_object_or_404(TOURNAMENT, pk=kwargs['pk'])
        context = {'tournament_view': tournament_view}
        return render(request, 'tournament_view.html', context)


class TournamentFormView(View):
    def get(self, request):
        tournament_form = TournamentForm()
        return render(request, 'tournament.html', context={'tournament_form': tournament_form})

    def post(self, request):
        tournament_form = TournamentForm(request.POST, request.FILES)
        if tournament_form.is_valid():
            TOURNAMENT.objects.create(**tournament_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'tournament.html', context={'tournament_form': tournament_form})

####### GAME


class GameFormView(View):
    def get(self, request):
        game_form = GameForm()
        return render(request, 'game.html', context={'game_form': game_form})

    def post(self, request):
        game_form = GameForm(request.POST, request.FILES)
        if game_form.is_valid():
            GAME.objects.create(**game_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'game.html', context={'game_form': game_form})


class GameListView(generic.ListView):
    model = GAME
    template_name = 'game_list.html'
    context_object_name = 'game_list'
    queryset = GAME.objects.all()[:100]


class GameDetailView(generic.DetailView):
    def get(self, request, *args, **kwargs):
        game_view = get_object_or_404(GAME, pk=kwargs['pk'])
        context = {'game_view': game_view}
        return render(request, 'game_view.html', context)


####### TEAM


class TeamFormView(View):
    def get(self, request):
        team_form = TeamForm()
        return render(request, 'team.html', context={'team_form': team_form})

    def post(self, request):
        team_form = TeamForm(request.POST, request.FILES)
        if team_form.is_valid():
            TEAM.objects.create(**team_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'team.html', context={'team_form': team_form})


class TeamListView(generic.ListView):
    model = TEAM
    template_name = 'team_list.html'
    context_object_name = 'team_list'
    queryset = TEAM.objects.all()[:100]


class TeamDetailView(generic.DetailView):
    def get(self, request, *args, **kwargs):
        team_view = get_object_or_404(TEAM, pk=kwargs['pk'])
        context = {'team_view': team_view}
        return render(request, 'team_view.html', context)
