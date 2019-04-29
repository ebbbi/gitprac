from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone
# Create your views here.

def home(request):
    posts=Post.objects.all
    return render(request, 'blog/home.html', {'posts':posts})

def new(request):
    if request.method=='POST':
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            author=request.user
            form.pub_date=timezone.now
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/new.html', {'form':form})
            
    