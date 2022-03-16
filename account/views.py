from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

# Create your views here.
def registration_view(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            form.save()
            new_account = authenticate(email=email, password=password)
            login(request, new_account)
            return redirect('home_page')
        else:
            context['form'] = form
    else:
        context['form'] = RegistrationForm(request.POST)
    return render(request, 'account/register.html', context)
