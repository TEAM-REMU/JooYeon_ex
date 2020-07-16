from django.shortcuts import render, redirect
from .models import Blog
from django.core.paginator import Paginator

# Create your views here.
def read_blog_list(request):
    blogs = Blog.objects.order_by('-created_date')
    paginator = Paginator(blogs, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    

    return render(request, 'blog_list.html', {'posts': posts})

def blog_new(request):
    return render(request, 'blog_new.html')

def create_blog(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.content = request.POST['content']
    blog.count=1
    blog.save()
    return redirect('read_blog_list')

def read_blog_one(request,pk):
    blog = Blog.objects.get(pk=pk)
    blog.count += 1
    blog.save()
    return render(request, 'blog_detail.html', {'blog':blog})

def update_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.title = request.POST['title']
    blog.content = request.POST['content']
    blog.save()
    return redirect('read_blog_list')

def delete_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.delete()
    return redirect('read_blog_list')

