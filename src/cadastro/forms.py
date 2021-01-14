from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth import password_validation

User = get_user_model()

class CadastroFormulario(forms.Form):
	nome 				= 	forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))
	sobrenome			= 	forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))
	username			=	forms.CharField(max_length=120, label='Usuário', widget=forms.TextInput(attrs={'class': 'form-control'}))
	email				= 	forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	senha				= 	forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',}))
	confirma_senha 		=	forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',}))

class LoginForm(forms.Form):
	username 	= forms.CharField(max_length=120, label='Usuário', widget=forms.TextInput(attrs={'class': 'form-control'}))
	senha 		= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',}))	
