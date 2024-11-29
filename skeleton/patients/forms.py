from django import forms
from .models import patientAppointment

class PatientAppointmentForm(forms.ModelForm):
    class Meta:
        model = patientAppointment
        fields = '__all__'  # Use this to include all fields from the model. Alternatively, list specific fields.
        
    
        
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'patient': forms.TextInput(attrs={'class': 'form-control disable', }),
            'preferred_appointment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'preferred_time': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'reason_for_visit': forms.Textarea(attrs={'class': 'form-control'}),
            'symptoms': forms.Textarea(attrs={'class': 'form-control'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_relationship': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_number': forms.TextInput(attrs={'class': 'form-control'}), 
        }
