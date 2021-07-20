from django import forms


class SignInForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField()
