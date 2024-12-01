from django import forms
from .models import DoctorProfile, CustomUser, PatientProfile, InstitutionProfile, InstitutionDoctorProfile


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
            'doctor': forms.TextInput(attrs={'class': 'form-control'}),
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
            'patient': forms.TextInput(attrs={'class': 'form-control'}),
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
        fields = [
            'institution',
            'registration_number',
            'address',
            'city',
            'state',
            'country',
            'phone_number',
            'email',
            'website',
            'established_date',
            'description'
        ]
        
        widgets = {
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
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

class InstitutionDoctorProfileForm(forms.ModelForm):
    class Meta:
        model = InstitutionDoctorProfile
        fields = '__all__'
        widgets = {
            'doctor': forms.TextInput(attrs={'class': 'form-control'}),
            'institution': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'employee_id': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
        }