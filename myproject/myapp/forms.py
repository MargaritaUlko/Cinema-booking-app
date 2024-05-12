from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Movie1
from .models import User

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie1
        fields = ['title', 'description', 'poster']
