from django import forms
from .models import DoctorProfile, CustomUser, PatientProfile


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
            'profile',
        ]
        widgets = {
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.Select(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control'}),
            'license_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'profile': forms.ClearableFileInput(attrs={'class': 'form-control'}),
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