from django.shortcuts import render
from .models import SearchQuery

from blog.models import BlogPost

# Create your views here.
def search_view(request):
	query 		= request.GET.get('q', None)
	user 		= None

	if request.user.is_authenticated:
		user = request.user

	context = {
		'query': query,
		'page_title': f'Pesquisa: {query}'  
	}

	if query is not None:
		SearchQuery.objects.create(user=user, query=query)
		result_list = BlogPost.objects.search(query=query)
		context['result_list'] = result_list
	template_name = 'searches/view.html'
	return render(request, template_name, context)