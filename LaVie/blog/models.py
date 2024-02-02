import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from time import time
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.filter(is_superuser=True).first().pk)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)
#a comments field for each article
    comments = models.ManyToManyField('Comment', related_name='article_comments', blank=True)
    #created_by = user.username

    def get_absolute_url(self):
        if not self.slug:
            self.slug = slugify(self.title)
            self.save()
        return reverse("detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
            #self.save()
        return super(Article, self).save(*args, **kwargs)        
    

#code to show recently published articles
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
    def __str__(self):
        return self.title

#a new model to handle comments for each article
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.author} on {self.pub_date}'        