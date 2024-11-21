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