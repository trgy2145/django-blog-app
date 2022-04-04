from django.db import models
from django.contrib.auth.models import User
from users.forms import UserForm   
from users.models import Profile
from django.urls import reverse
from django.conf import settings
from django.utils.timezone import now

# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=130)
    content = models.TextField()
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    dateTime = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now=True)

    Category = (
        ("1", "Django"),
        ("2", "React"),
        ("3", "Python"),
       
    )

    Status = (
        ("D", "Draft"),
        ("V", "View"),
    )

    category = models.CharField(max_length=50, choices=Category, default='3')
    status = models.CharField(max_length=6, choices=Status, default='D')
    likes = models.ManyToManyField(User, related_name='blog_posts')
    post_views = models.IntegerField(default=0, null=True, blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.author} {self.title}"

    # def get_absolute_url(self):
    #     return reverse('detail')

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    body = models.TextField()
    dateTime = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.post.title}{self.name}"        