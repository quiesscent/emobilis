from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    services = Service.objects.all()
    faqs = Faqs.objects.all()
    about = About.objects.all()
    features = Features.objects.all()
    
    context = {
        'blogs': blogs,
        'services': services,
        'faqs': faqs,
        'abouts': about,
        'features': features,
    }
    return render(request, 'index.html', context)


def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})
    

def about(request):
    blogs = Blog.objects.all()
    faqs = Faqs.objects.all()
    about = About.objects.all()
    features = Features.objects.all()
    
    context = {
        'blogs': blogs,
        'faqs': faqs,
        'abouts': about,
        'features': features,
    }
    return render(request, 'about.html', context)
    

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html',{'blogs': blogs})
    

def contact(request):
    return render(request, 'contact.html')
    