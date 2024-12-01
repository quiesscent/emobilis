from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=90)
    description = models.CharField(max_length=200, default='')
    content = models.TextField(default='')
    image = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Contact(models.Model):
    name = models.CharField(max_length=10, default='')
    email = models.EmailField(default='user@gmail.com')
    subject = models.CharField(max_length=20000, default='')
    message = models.TextField(max_length=20000, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Subscribers(models.Model):
    email = models.EmailField(default='user@gmail.com')

    def __str__(self):
        return self.email
    
class Service(models.Model):
    title = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='services/', default='image.jpg')
    content = models.TextField(max_length=100000, default='')

    def __str__(self):
        return f'{self.title}'

class Features(models.Model):
    title = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=50, default='')
    content = models.TextField(max_length=100000, default='')

    def __str__(self):
        return f'{self.title}'

class Faqs(models.Model):
    questiion = models.CharField(max_length=100)
    answer = models.TextField(default='')

    def __str__(self):
        return f'{self.questiion}'
   
    
class About(models.Model):
    content = models.TextField(max_length=100000, default='')

    def __str__(self):
        return f'About'