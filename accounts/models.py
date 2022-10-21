from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import Count


# Create your models here.

STATUS = (
    ("Draft","Draft"),
    ("Publish","Publish")
)

class Post(models.Model):
    photo=models.ImageField(blank=True,null=False,upload_to='images/')
    title=models.CharField(max_length=255, null=True)
    slug=models.SlugField(max_length=255, null=True)
    description=RichTextUploadingField(blank=True,null=True)
    blog_views=models.IntegerField(default=0)
    status = models.CharField(max_length=255,choices=STATUS, default="Publish")
    user_id = models.IntegerField(blank=True)
    date_added= models.DateTimeField(auto_now_add=True)   
    

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

class Comment(models.Model):
    name=models.CharField(max_length=100,null=False,blank=True)
    body=models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commen',null=False, default='')
    date_added= models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.name


