from django.shortcuts import render
from .models import Post


def post(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    
    return render(request=request, 
                  template_name='main_app/index.html',
                  context=context)
