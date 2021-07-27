from django import forms


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class AddUser(forms.Form):
    username = forms.CharField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()