from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def index(request):
    return HttpResponse("Hello dear, welcome!")

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'blog/detail.html', {'article': article})


