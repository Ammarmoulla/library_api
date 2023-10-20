from django.db import models

# Create your models here.
class Book(models.Model):
    slug = models.SlugField(max_length=250)
    title = models.CharField(max_length=250)
    body = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    
    def __str__(self):
        return self.title