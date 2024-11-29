from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser
# Create your views here.

# patient register
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        check_user = True if CustomUser.objects.filter(username=username).exists() else False
        if check_user:
            message.error(request, "Username Already Taken")
            return redirect("acc:register")

        if password2 != password:
            messages.error(request, 'Passwords do not match')
            return redirect("acc:register")

        else:
            user = CustomUser.objects.create_user(
                    email=email,
                    username=username,
                    password=password2,
                    user_type='patient',
                    institution='None' 
                )
            user.save()
        messages.success(request, 'Welcome to MediSphere, Login to Access Dashboard')
        return redirect('acc:login')

    return render(request, 'register.html')

# institution registration
def register_inst(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        check_user = True if CustomUser.objects.filter(username=username).exists() else False
        if check_user:
            message.error(request, "Username Already Taken")
            return redirect("acc:register")

        if password2 != password:
            messages.error(request, 'Passwords do not match')
            return redirect("acc:register")

        else:
            user = CustomUser.objects.create_user(
                    email=email,
                    username=username,
                    password=password2,
                    user_type='institution',
                    institution=username,
                )
            user.save()
        messages.success(request, 'Welcome to MediSphere, Login to Access Dashboard')
        return redirect('acc:login')

    return render(request, 'auth/institution.html')


# independent doctor registration
def register_doc(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        check_user = True if CustomUser.objects.filter(username=username).exists() else False
        if check_user:
            message.error(request, "Username Already Taken")
            return redirect("acc:register")

        if password2 != password:
            messages.error(request, 'Passwords do not match')
            return redirect("acc:register")

        else:
            user = CustomUser.objects.create_user(
                    email=email,
                    username=username,
                    password=password2,
                    user_type='doctor',
                )
            user.save()
        messages.success(request, 'Welcome to MediSphere, Login to Access Dashboard')
        return redirect('acc:login')

    return render(request, 'auth/doctor.html')

# default login
def login_(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back { user.username }")
            if user.user_type == 'patient':
                return redirect('patients:dashboard')

            elif user.user_type == 'doctor':
                return redirect('doctors:dashboard')

            elif user.user_type == 'institution':
                return redirect('institutions:dashboard')
            else:
                return redirect('core:home')
        else:
            messages.error(request, 'Invalid email or password. Contact Institution or Register')

    return render(request, 'login.html')


def logout_(request):
    logout(request)
    messages.success(request, 'Goodbye, See you again')
    return redirect('core:home')