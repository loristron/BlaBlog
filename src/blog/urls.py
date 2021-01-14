from django.urls import path

from .views import (
    blog_post_detail_view,
    blog_post_list_view,
    blog_post_update_view,
    blog_post_delete_view,
    )

urlpatterns = [

    path('', blog_post_list_view, name='list-posts'),
    path('<str:slug>/', blog_post_detail_view, name='post-detail'),
    path('<str:slug>/edit', blog_post_update_view, name='post-edit'),
    path('<str:slug>/delete', blog_post_delete_view, name='post-delete'),

]
