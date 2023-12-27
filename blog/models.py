from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model): # database will now have the table called the post and inside the post, one of the fieds that table will have will be the title.
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)#it means if the usr is deleted, it delets post too.
    
    def get_absolute_url(self):
         return reverse('post-detail', kwargs={'pk': self.pk})
    def __str__(self):
       return self.title


