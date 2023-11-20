from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import BlogForm

#@login_required
def index(request):
    if request.user.is_authenticated:
        return render(request, 'blog/index.html', {'user': request.user})
    else:
        return render(request, 'blog/index.html')    
    
@login_required
def create_article(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')#redirect to article_list view
    else:
        form = BlogForm()
    return render(request, 'blog/create.html', {'form': form})                

@login_required
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

@login_required
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'blog/detail.html', {'article': article})


