from django.contrib import admin
from django.urls import path
import post.views
#from .import views

urlpatterns = [
    path('blog/list', post.views.read_blog_list, name = 'read_blog_list'),
    path('blog/new', post.views.blog_new, name = 'blog_new'),
    path('blog/create', post.views.create_blog, name = 'create_blog'),
    path('blog/detail/<int:pk>', post.views.read_blog_one, name = 'read_blog_one'),
    path('blog/update/<int:pk>', post.views.update_blog, name='update_blog'),
    path('blog/delete/<int:pk>', post.views.delete_blog, name='delete_blog'),
]