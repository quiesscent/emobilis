from django import forms
from .models import DoctorProfile, CustomUser, PatientProfile, InstitutionProfile


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
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'adress': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'profile': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            # Filter users by user_type
        self.fields['patient'].queryset = CustomUser.objects.filter(user_type='patient')
            
class InstitutionProfileForm(forms.ModelForm):
    class Meta:
        model = InstitutionProfile
        fields = '__all__'
        
        widgets = {
            'institution': forms.Select(attrs={'class': 'form-control'}),
            'registration_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'established_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 8, 'class': 'form-control', 'rows': 4}),
        }