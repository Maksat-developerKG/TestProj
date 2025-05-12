from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login




def reg_log_view(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'signup':
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 != password2:
                messages.error(request=request, 
                               message='Password do not match')
            elif User.objects.filter(username=username).exists():
                messages.error(request=request,
                               message='Username already exists')
            else:
                User.objects.create_user(username=username, email=email, password=password1)
                messages.success(request=request, 
                                 message='Account created successfully')
                return redirect('home')
            
        elif form_type == 'login':
            email = request.POST['email']
            password = request.POST['password']

            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request=request, user=user)
                    return redirect('home')
                else:
                    messages.error(request=request, 
                                   message='Incorrect password')
                    
            except User.DoesNotExist:
                messages.error(request=request, 
                               message='User not found')
    
    return render(request=request, template_name='accounts/reg_log.html')