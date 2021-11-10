from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from sber_games.models import USER


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'main'
        context['title'] = 'Sber CyberGame'
        context['description'] = 'Sber CyberGame'
        return context


def registration(request, *args, **kwargs):
    return render(request, 'registration.html', {})


def user_info(request, *args, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    return render(request, 'user_info.html', {'ip_adress': ip})
