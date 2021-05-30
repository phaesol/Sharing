from django.db import models
from accounts.models import Profile



class Category(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="categories")
    category = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category

class Post(models.Model):
  
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="posts")
    image = models.ImageField(upload_to='url_images',blank=True,null=True)
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True) 
    url = models.URLField (max_length=400) #default 200
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


