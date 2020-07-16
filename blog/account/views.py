from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    # 회원가입 기능
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"], password = request.POST["password2"]
            )
            auth.login(request,user)
            return redirect('read_blog_list')
    # request를 받은 곳에 signup.html을 보여줘!
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password =  password)
        if user is not None:
            auth.login(request, user)
            return redirect('read_blog_list')
        else:
            return render (request, 'login.html', {'error': 'username or password is incorrect'})
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('read_blog_list')