from django.shortcuts import render, HttpResponse
from .models import Hotel, Quarto, Usuario
from .forms import FormNome, formCadastroUsuario, FormLogin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.conf import settings
from django.shortcuts import redirect

def reservas(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    dados_quarto = Quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    if request.method == 'POST':
        form = FormNome(request.POST)
        if form.is_valid():

            var_nome = form.cleaned_data['nome']          # pega o nome do form
            var_email = form.cleaned_data['email']        # pega o email do form
            var_idade = form.cleaned_data['idade']        # pega a idade do form
            var_data = form.cleaned_data['data']          # pega a data do form
            var_quartos = form.cleaned_data['quartos']    # pega a quantidade de quartos do form

            print(var_nome, var_email, var_idade, var_data)


            usuario = Usuario(nome=var_nome, email=var_email, idade=var_idade, data=var_data, quartos=var_quartos) # cria um objeto do tipo Usuario
            usuario.save() # salva o objeto no banco de dados
        
            return HttpResponse('<h1>thanks</h1>')
    else:
        form = FormNome()
        context['form'] = form
        return render(request, 'reservas.html', context)


def homepage(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    dados_quarto = Quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    if request.user.is_authenticated:
        return render(request,'homepage2.html', context)
    else:
        return render(request,'homepage.html', context)

def quartos(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    dados_quarto = Quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    return render(request,'quartos.html', context)

def cadastro_usuario(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    dados_quarto = Quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    if request.method == 'POST':
        form = formCadastroUsuario(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['first_name']
            var_sobrenome = form.cleaned_data['last_name']
            var_usuario = form.cleaned_data['user']
            var_email = form.cleaned_data['email']
            var_senha = form.cleaned_data['password']

            user = User.objects.create_user(username=var_usuario, email=var_email, password=var_senha)
            user.first_name = var_nome
            user.last_name = var_sobrenome
            user.save()
            return redirect('/login') 
    else:
        form = formCadastroUsuario()
        context['form'] = form
        return render(request, 'cadastro_usuario.html', context)

def login(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    dados_quarto = Quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():

            var_usuario = form.cleaned_data['user']
            var_senha = form.cleaned_data['password']
            
            user = authenticate(username=var_usuario, password=var_senha)

            if user is not None:
                auth_login(request, user)
                return redirect('/')  
            else:
                print('Login falhou')
    else:
        form = FormLogin()
        context['form'] = form
        return render(request, 'login.html', context)
    
def logout(request):
    auth_logout(request)
    return redirect('/')
