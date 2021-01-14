from django.shortcuts import render, redirect
from .forms import CadastroFormulario, LoginForm
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib import messages

# Create your views here.

User = get_user_model()
def pagina_cadastro_view(request):
	validado 			= True
	user 				= None
	form 				= CadastroFormulario(request.POST or None)
	if form.is_valid():
		nome			= form.cleaned_data.get('nome')
		sobrenome		= form.cleaned_data.get('sobrenome')
		username 		= form.cleaned_data.get('username')
		email			= form.cleaned_data.get('email')
		senha			= form.cleaned_data.get('senha')
		confirma_senha 	= form.cleaned_data.get('confirma_senha')

		try: 
			if senha != confirma_senha:
				messages.info(request, 'Senhas Diferentes!')
				validado = False

			qs = User.objects.filter(username__iexact=username)
			if qs.exists():
				messages.info(request, 'Usuário já existe')
				validado = False

			qs = User.objects.filter(email__iexact=email)
			if qs.exists():
				messages.info(request, 'Email Já cadastrado. ')
				validado = False
		except:
			messages.info(request, 'Senha fraca!')
			validado = False

		if validado == True:
			try:
				user = User.objects.create_user(username, email=email, password=senha, first_name=nome, last_name=sobrenome)
			except:
				user = None
				messages.info(request, 'Algo deu errado. Por favor, tente novamente')
		if user != None:
			login(request, user)
			return redirect('/')
	context 		= {
		'form': 		form,
		'page_title': 	'Cadastro'
	}

	template_name	= 'cadastro/cadastro.html'
	return render(request, template_name, context)

def login_page_view(request):
	form 					= LoginForm(request.POST or None)
	if form.is_valid():
		username 			= form.cleaned_data.get('username')
		senha 				= form.cleaned_data.get('senha')
		user 				= authenticate(request, username=username, password=senha)
		if user == None:
			messages.info(request, 'Usuário ou senha inválidos')
		else:
			login(request, user)
			return redirect('/')
	context 			= {'login_form': form, 'page_title': 'Fazer Login'}
	template_name 		= 'cadastro/login.html'
	return render(request, template_name, context)

def logout_view(request):
	logout(request)
	return redirect('/')
