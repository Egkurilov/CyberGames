from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
# Create your views here.
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from app_profiles.models import USER
from sber_games.forms import TournamentForm
from sber_games.models import TOURNAMENT


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
        print(request.POST)
        if tournament_form.is_valid():
            TOURNAMENT.objects.create(**tournament_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'tournament.html', context={'tournament_form': tournament_form})
