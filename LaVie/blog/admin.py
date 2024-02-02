from django.contrib import admin
from .models import Article, Comment

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "content",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
