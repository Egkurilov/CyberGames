from django import forms


class UserForm(forms.Form):
        nickname = forms.CharField()
        password = forms.CharField()
        first_name = forms.CharField()
        second_name = forms.CharField()
        last_name = forms.CharField()
        email = forms.EmailField()
        tab_number = forms.CharField()
        game_account = forms.CharField()
