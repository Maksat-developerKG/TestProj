from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login




def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request=request, 
                                  message='Password do not match')
            return render(request=request,
                          template_name='accounts/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request=request, message='Usernmae already exists')
            return render(request=request,template_name='accounts/register.html')
        
        user = User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request=request,
                         message='Accounts created successfully')
        return redirect('login')
    return render(request=request,
                  template_name='accounts/register.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            user = authenticate(request=request, uesrname=user.username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request=request, message='Incorrect password')
        except User.DoesNotExist:
            messages.error(request=request, 
                           message='User with this email not found')
            
    return render(request=request, template_name='accounts/login.html')


