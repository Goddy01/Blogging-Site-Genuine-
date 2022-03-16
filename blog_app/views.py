import imp
from django.shortcuts import render
from account.models import Account

# Create your views here.
def home_page(request):
    accounts = Account.objects.all()
    context = {
        'accounts': accounts
    }

    return render(request, 'blog_app/home.html', context)