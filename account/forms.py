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
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                print('fuck you son of a bitch')
                raise forms.ValidationError('Invalid login details')
                