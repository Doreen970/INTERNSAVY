from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from .forms import BlogForm

def index(request):
    return HttpResponse("Hello dear, welcome!")

def create_article(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')#redirect to article_list view
    else:
        form = BlogForm()
    return render(request, 'blog/create.html', {'form': form})                

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'blog/detail.html', {'article': article})


