from django.shortcuts import render
from django.http import HttpResponse
from .forms import DoctorProfileForm, PatientProfileForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def register(request):
    form = CustomUserCreationForm()
    if request.method ==  'POST':
        if form.is_valid:
            form.save()
            messages.success(request, "User Created Successfully")
    context = {
        'form': form
    }
    return render(request, 'register.html', context)
    
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages(request, f"Welcome backn{user.username}")
            return redirect('/') 
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')