import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.filter(is_superuser=True).first().pk)
    #created_by = user.username
    

#code to show recently published articles
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
    def __str__(self):
        return self.title