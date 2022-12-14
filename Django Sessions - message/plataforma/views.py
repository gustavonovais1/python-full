from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    if request.session.get('logado'):
        return render(request, 'home.html')
    else:
        return redirect('/auth/login/?status=2')