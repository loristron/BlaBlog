 #change what a page looks like

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template

from blog.models import BlogPost

from .forms import ContacForm

def home_page_view(request):
	qs = BlogPost.objects.published()[:3]
	context = {
		"page_title": 'Página Inicial',
		"post_list": qs,
		'homepage': True,
	}
	return render(request, 'home.html', context)

def about_page_view(request):
	context = {"page_title": 'Sobre Nós'}
	return render(request, 'about.html', context)

def contact_page_view(request):
	form = ContacForm(request.POST or None)
	context = {
		"page_title": 'Contato',
		'form': form,
	}	
	if form.is_valid():
		print(form.cleaned_data)
		form = ContacForm()
		return redirect('/')
	return render(request, 'contact.html', context)

##EXEMPLO DE RENDERIZAÇÃO POR HTTPRESPONSE
# def example_page_view(request):
# 	context				= {'page_title': 'Exemplo'}
# 	template_name 		= "hello_world.html"
# 	template_obj 		= get_template(template_name)
# 	rendered_item 		= template_obj.render(context)
# 	return HttpResponse(rendered_item)