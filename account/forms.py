import email
from unittest import expectedFailure
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Account
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text='Provide a valid email address.')
    class Meta():
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    class Meta():
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')

            user = authenticate(email=email, password=password)
            if not user:
                print('you a bitch')
                raise forms.ValidationError("Invalid login details.")



