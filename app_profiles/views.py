from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from app_profiles.forms import UserForm

# Create your views here.
from app_profiles.models import register_USER


class UserFormView(View):
    def get(self, request):
        user_form = UserForm()
        return render(request, 'profiles/registration.html', context={'user_form': user_form})

    def post(self, request):
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            register_USER.objects.create(**user_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'profiles/registration.html', context={'user_form': user_form})
