from django import forms
from .models import BlogPost

class BlogPostForm(forms.Form): #esse não tá sendo usado não 
	postTitle 		= forms.CharField()
	postContent		= forms.CharField(widget=forms.Textarea)
	#slug 			= forms.SlugField()

class BlogPostModelForm(forms.ModelForm):
	class Meta:
		model 	= BlogPost
		fields 	= ['postTitle', 'postContent', 'image', 'publish_date']
		labels 	= {
			'postTitle': 'Título', 
			'postContent': 'Conteúdo', 
			'image': "Enviar Imagem", 
			'publish_date': 'Data de Publicação',
			}
		widgets = {
		'postTitle': forms.TextInput(attrs={'class': 'form-control'}),
		'postContent': forms.Textarea(attrs={'class': 'form-control'})
		}

	def clean_postTitle(self, *args, **kwargs): #é importante que o método tenha o mesmo nome que os campos!!!
		instance = self.instance
		postTitle = self.cleaned_data.get('postTitle')
		qs = BlogPost.objects.filter(postTitle__iexact=postTitle)
		if instance is not None:
			qs.exclude(pk=instance.pk)
		if qs.exists():
			raise forms.ValidationError('Este título já está sendo usado. Tente novamente')
		return postTitle


class UpdateBlogPostForm(forms.ModelForm):
	class Meta:
		model 	= BlogPost
		fields 	= ['postTitle', 'postContent', 'image', 'publish_date']
		labels 	= {
			'postTitle': 'Título', 
			'postContent': 'Conteúdo', 
			'image': "Enviar Imagem", 
			'publish_date': 'Data de Publicação',
			}
		widgets = {
		'postTitle': forms.TextInput(attrs={'class': 'form-control'}),
		'postContent': forms.Textarea(attrs={'class': 'form-control'})
		}

	def save(self, commit=True):

		blog_post = self.instance
		blog_post.postTitle = self.cleaned_data['postTitle']
		blog_post.postContent = self.cleaned_data['postContent']

		if self.cleaned_data['image']:
			blog_post.image = self.cleaned_data['image']
		if commit: 
			blog_post.save()
		return blog_post

	
	# def clean_postTitle(self, *args, **kwargs): #é importante que o método tenha o mesmo nome que os campos!!!
	# 	instance = self.instance
	# 	postTitle = self.cleaned_data.get('postTitle')
	# 	qs = BlogPost.objects.filter(postTitle__iexact=postTitle)
	# 	if instance is not None:
	# 		qs.exclude(pk=instance.pk)
	# 	if qs.exists():
	# 		raise forms.ValidationError('Este título já está sendo usado.')
	# 	return postTitle