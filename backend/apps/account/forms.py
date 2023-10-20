from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm



class LoginForm(forms.Form):
    username = forms.CharField(label='Username',
                             widget=forms.TextInput(attrs={'class':'form-control',
                                                           "placeholder": "Enter your username"}))

    # email = forms.EmailField(
    #     label="Электронная почта",
    #     widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Почта"})
    # )
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(
                                   attrs={'class':'form-control',
                                          'type':'password',
                                          "placeholder": "Enter your password",
                                          'autocomplete':'off'}))

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',"placeholder": "Enter your passwod"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',"placeholder": "Repeat your password"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "Enter your username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',"placeholder": "Enter your email"}))

    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]



