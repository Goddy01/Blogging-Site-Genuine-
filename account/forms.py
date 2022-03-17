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
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = Account
        fields = ('email', 'password')


    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned.get(email)

        if authenticate(email=email, password=password) == False:
            raise forms.ValidationError('Invalid login details')