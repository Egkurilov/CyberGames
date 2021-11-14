from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.views.generic import TemplateView

from app_profiles.models import USER


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


def user_profile(request, *args, **kwargs):
    users = USER.objects.all()
    return render(request, 'user_profile.html', {'users': users})


def registration(request, *args, **kwargs):
    return render(request, '../app_profiles/templates/profiles/registration.html', {})


def my_game(request, *args, **kwargs):
    return render(request, 'my_game.html', {})


def my_team(request, *args, **kwargs):
    return render(request, 'my_team.html', {})


def tournament(request, *args, **kwargs):
    return render(request, 'tournament.html', {})


def user_info(request, *args, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    return render(request, 'user_info.html', {'ip_adress': ip})
