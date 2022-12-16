from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login')
def home(request):
    return render(request, 'home.html')