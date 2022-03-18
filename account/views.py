from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AccountUpdateForm, RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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
        context['form'] = RegistrationForm()
    return render(request, 'account/register.html', context)

@login_required
def logout_view(request):
    """For logging out"""
    logout(request)
    return redirect('home_page')
    # return HttpResponse('logged out')


def login_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('home_page')
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home_page')
    else:
        login_form = LoginForm()
    context['login_form'] = login_form
    return render(request, 'account/login.html', context)
    

@login_required
def update_view(request):
    context = {}

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        update_form = AccountUpdateForm(request.POST)
        if update_form.is_valid():
            update_form.save()
    else:
        update_form = AccountUpdateForm()
    context['update_form'] = update_form
    return render(request, 'account/account.html', context)