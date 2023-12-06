from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:pk>/', views.detail, name='detail'),
    path('create/', views.create_article, name='create_article'),
    path('dashboard/', views.dashboard, name='user_dashboard'),
]