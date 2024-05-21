from django import forms
from .models import Quarto

class FormNome(forms.Form):
    nome = forms.CharField(label="Seu nome", max_length=40)
    email = forms.EmailField(label="Seu e-mail")
    idade = forms.IntegerField(label="Sua idade")
    data = forms.DateField(label="Data de agendamento", widget=forms.DateInput(attrs={'type': 'date'}))
    quartos = forms.CharField(label="Quantidade de quartos")
    # Campo de seleção dropdown
    quartos = forms.ModelChoiceField(queryset=Quarto.objects.all())
    

class formCadastroUsuario(forms.Form):
    first_name = forms.CharField(label="Nome", max_length=40)
    last_name = forms.CharField(label="Sobrenome", max_length=40)
    user = forms.CharField(label="Usuário", max_length=40)   
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)


class FormLogin(forms.Form):
    user = forms.CharField(label="Usuario", max_length=40)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)