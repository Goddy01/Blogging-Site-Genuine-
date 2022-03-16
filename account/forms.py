from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text='Provide a valid email address.')
    class Meta():
        model = Account
        fields = ('email', 'username', 'password1', 'password2')