from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import BlogForm, EditForm
from django.db.models import Q

#@login_required
def index(request):
    articles = Article.objects.all()
    if request.user.is_authenticated:
        return render(request, 'blog/index.html', {'user': request.user, 'articles': articles})
    else:
        return render(request, 'blog/index.html', {'articles': articles}) 

def search(request):
    query = request.GET.get('q')
    
    qs = Article.objects.all()
    if query is not None:
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        qs = Article.objects.filter(lookups)
        context = {
            "object_list": qs
        }
    return render(request, 'blog/search.html', context=context)                  
    
@login_required
def create_article(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.created_by = request.user
            article.save()
            return redirect('article_list')#redirect to article_list view
    else:
        form = BlogForm()
    return render(request, 'blog/create.html', {'form': form})                

@login_required
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

@login_required
def detail(request, slug):
    #article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, slug=slug)
    #article = Article.objects.get(slug=slug)
    return render(request, 'blog/detail.html', {'article': article})

@login_required
def dashboard(request):
    user_articles = Article.objects.filter(created_by=request.user)
    return render(request, 'blog/dashboard.html', {'user_articles': user_articles})

@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk, created_by=request.user)
    user_articles = Article.objects.filter(created_by=request.user)
    article.delete()
    return render(request, 'blog/dashboard.html', {'user_articles': user_articles})

@login_required
def edit(request, slug):
    article = Article.objects.get(id=slug, created_by=request.user)
    if request.method == 'POST':
        form = EditForm(request.POST, files=request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.created_by = request.user
            article.save()
            return redirect('detail', slug=article.slug)#redirect to detail view
    else:
        form = EditForm(instance=article)
    return render(request, 'blog/edit.html', {'form': form})        


