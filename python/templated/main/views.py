from django.shortcuts import render, redirect
from .models import Contact, Order
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def portfolio(request):
    return render(request, 'achievements.html')


def pricing(request):
    return render(request, 'pricing.html')


@csrf_exempt
def quote(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        tel = request.POST['tel']
        business= request.POST['business']
        service = request.POST['service']
        city = request.POST['city']
        communication = request.POST['communication']
        order = Order(name=name, email=email, tell=tel, business=business, service=service, city=city, communication_preference=communication)
        order.save()
        messages.success(request, "Your order has been recieved successfully, we will communicate shortly")
        return redirect('index')

    return render(request, 'quote.html')


@csrf_exempt
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, "Message Sent Successfully")
        return redirect('index')

    return render(request, 'contact.html')
