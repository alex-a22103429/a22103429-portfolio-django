from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField(max_length=250)
    birthDate = models.DateField()
    email = models.CharField(null=False)
    phone = models.IntegerField(null=False)
    verified = models.BooleanField(null=False)


    def __str__(self):
        return self.email

class Post(models.Model):
    title = models.IntegerField(max_length=250, null=False)
    content = models.CharField(max_length=1000, null=False)
    Date = models.DateField(null=False)
    image = models.ImageField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE,related_name= "posts")


    def __str__(self):
        return self.title
