from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from hashlib import sha256  
from django.contrib import messages, auth
from django.contrib.messages import constants
from .models import Users 

def login(request):
    if request.user.is_authenticated:
        return redirect('/plataforma/home')
    return render(request, 'login.html')

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/plataforma/home')
    return render(request, 'cadastro.html')

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    cep = request.POST.get('cep')
    rua = request.POST.get('rua')
    numero = request.POST.get('numero')

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        messages.add_message(request, constants.WARNING, 'Nome e email não podem estár vazios.')
        return redirect('/auth/cadastro/')

    if len(senha) < 8:
        messages.add_message(request, constants.WARNING, 'Sua senha deve ter no mínimo 8 caracteres')
        return redirect('/auth/cadastro/?')

    if Users.objects.filter(email=email).exists():
        messages.add_message(request, constants.ERROR, 'Email já cadastrado no sistema')
        return redirect('/auth/cadastro/')

    if Users.objects.filter(username=nome).exists():
        messages.add_message(request, constants.ERROR, 'Usuário já cadastrado no sistema')
        return redirect('/auth/cadastro/')

    try:
        usuario = Users.objects.create_user(username=nome, email=email, password=senha, cep=cep, rua=rua, numero=numero)
        usuario.save()

        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso!')
        return redirect('/auth/cadastro/')
    except:
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema.')
        return redirect('/auth/cadastro/')

def valida_login(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')

    usuario = auth.authenticate(request, username = nome, password = senha)
    
    print(senha, nome)
    if not usuario:
        messages.add_message(request, constants.WARNING, 'Email ou senha inválidos.')
        return redirect('/auth/login')
    else:
        auth.login(request, usuario)
        return redirect('/plataforma/home')

def sair(request):
    auth.logout(request)
    messages.add_message(request, constants.ERROR, 'Faça login antes de acessar a plataforma')
    return redirect('/auth/login/')