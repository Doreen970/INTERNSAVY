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
    #image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)
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

        