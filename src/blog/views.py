from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone 
from django import forms

from .models import BlogPost
from .forms import BlogPostForm, BlogPostModelForm, UpdateBlogPostForm

# Create your views here.

	#CRUD -> Create, retrieve, update and delete
	
	# GET -> retrieve, listar
	
	# POST -> create, update and delete


#CREATE
#cria objetos, cria postagens
#formulário (ainda não criado)

@login_required
#@staff_member_required
def blog_post_create_view(request):

		# SE O USUÁRIO NÃO ESTÁ LOGADO
		# if not request.user.is_authenticated:
			# return render(request, template_name, context={})

		# esse bloco seria útil pra passar esses dados pra vários formulários 
		# pTitulo	= form.cleaned_data['postTitle']  
		# pContent 	= form.cleaned_data['postContent']
		# pSlug		= form.cleaned_data['slug']

		#essa outra linha seria pra gente usar o formulário em: form = BlogPostForm(request.POST or None)
		# obj = BlogPost.objects.create(**form.cleaned_data)
		# obj.postTitle 	= form.cleaned_data.get('postTitle') + ' + teste!' -> adicionando coisas aos campos
		
		#pra manipular os dados antes de salvar atribuindo pra uma variável, obj
	form = BlogPostModelForm(request.POST or None, request.FILES or None)
	template_name	= 'form.html'
	context			= {
		'page_title': 'Novo Post',
		'form': form,
		'navblog': True,
	}
	if form.is_valid(): 
		obj = form.save(commit=False) 
		obj.user = request.user # configura o usuário!
		obj.save()
		form = BlogPostModelForm()
		return redirect('/blog')
	return render(request, template_name, context)

#RETRIEVE DETAIL 
def blog_post_detail_view(request, slug): #retrive view = detail view 
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name 	= 'blog/detail.html'
	context 		= { 
		'object': obj,
		'page_title': obj.postTitle,
		'navblog': True,
	}
	return render(request, template_name, context)

#RETRIEVE BY LIST
def blog_post_list_view(request):
			#lista objetos
			#também dá pra fazer com pesquisas
		 	#qs 			= BlogPost.objects.all() #get ALL of the objects in the database, list of python objects
			#now 			= timezone.now()
			#qs				= BlogPost.objects.filter(publish_date__lte=now)
	qs 				= BlogPost.objects.all().published()
	#esse if mostra também os drafs dos usuários pra eles mesmos
	if request.user.is_authenticated:
	 	qs2			= BlogPost.objects.filter(user=request.user)
	 	qs 			= (qs | qs2).distinct()
	template_name 	= 'blog/list.html'

	context			= {
		'object_list': qs,
		'page_title': 'Postagens',
		'navblog': True,
	}
	return render(request, template_name, context)

#UPDATE
#@staff_member_required
@login_required
def blog_post_update_view(request, slug):
			##BLCOO DE CÓDIGO QUE NÃO FUNCIONOU
			##Não deu pra fazer o UPDATE com o mesmo formulário de criar blog. Foi criara uma
			##nova classe no forms.py apenas para lidar com o update, usando a função do save()
			# obj = get_object_or_404(BlogPost, slug=slug)
			# form = BlogPostModelForm(request.POST or None, instance=obj)
			# if form.is_valid():
			# 	obj.form.save(commit=False)
			# 	obj.save()
			# 	print('salvou?')
			# 	context= {'form': form, 'page_title':'sucesso!'}
			# else:
			# 	print('formulário inválido')
	
	#essa outra parte do código consegue lidar com o Update, mas usando a classe UpdateBlogPostForm 
	blog_post = get_object_or_404(BlogPost, slug=slug)
	if request.POST:
		form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			blog_post = obj
			return redirect('/blog')
		else:
			print('invalid form')
	form = UpdateBlogPostForm(
		initial={
			'postTitle': blog_post.postTitle,
			'postContent': blog_post.postContent,
			#'slug': blog_post.slug,
			'image': blog_post.image,
			'publish_date': blog_post.publish_date,
		}
	)

	context = {
		"page_title": "Modificar '"+ blog_post.postTitle + "'",
		'form': form, 
		'navblog': True,
		}
	template_name 	= 'form.html'
	return render(request, template_name, context)

#DELETE
@login_required
def blog_post_delete_view(request, slug):
	obj 			= get_object_or_404(BlogPost, slug=slug)

	if request.method == 'POST':
		obj.delete()
		return redirect('/blog')

	template_name	= 'blog/delete.html'
	context			= {
		'page_title': 'Delete '+ obj.postTitle,
		'object': obj,
		'navblog': True,
	}
	return render(request, template_name, context)