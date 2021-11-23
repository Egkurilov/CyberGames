from django import forms

from app_profiles.models import USER


class UserForm(forms.ModelForm):
        class Meta:
                model = USER
                fields = '__all__'
                exclude = ['teams', 'status']