"""djangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings

from blog.views import blog_post_create_view
from searches.views import search_view
from cadastro.views import pagina_cadastro_view, login_page_view, logout_view

from .views import ( 
	home_page_view,
	about_page_view,
	contact_page_view,
	
)
urlpatterns = [
    path('', home_page_view, name='home-page'),
    path('about/', about_page_view, name='about-page'),
    path('contact/', contact_page_view, name='contact-page'),
    
    path('blog-new/', blog_post_create_view, name='post-create'),
    path('admin/', admin.site.urls),

    path('blog/', include('blog.urls')),

    path('search/', search_view, name='search-page'),

    path('cadastro/', pagina_cadastro_view, name='cadastro'),
    path('login/', login_page_view, name='login'),
    path('logout/', logout_view, name='logout')

]

#se o projeto ainda está em desenvolvimento no servidor django. Se tiver em outro servidor esse tratamento
#se dá de outra maneira, mais automática dependendo do servidor 
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)