from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import DoctorProfile, CustomUser, PatientProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username']


class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = [
            'doctor',
            'date_of_birth',
            'gender',
            'phone_number',
            'specialization',
            'license_no',
            'department',
            'profile',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = [
            'patient',
            'date_of_birth',
            'gender',
            'phone_number',
            'adress',
            'emergency_contact_name',
            'emergency_contact_number',
            'profile',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }