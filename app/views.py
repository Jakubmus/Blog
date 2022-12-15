from django.shortcuts import render
from .models import Post

def base(request):
    posts = Post.objects.all()
    return render(request, 'app/base.html', {'posts': posts})
def read(request,id):
    post = Post.objects.get(id=id)
    return render(request, 'app/read.html', {'post': post})