from accounts.models import Profile
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class Write(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    contents = models.TextField()
    images = models.ImageField(null=True, blank=True)
    updated_at = models.DateField(auto_now=True)
    like_count = models.PositiveIntegerField(default=0)
    
class Comment(models.Model):
    post = models.ForeignKey(Write, related_name="comment", on_delete=CASCADE)
    user = models.ForeignKey(User,related_name="comment", on_delete=CASCADE)
    content = models.TextField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title
