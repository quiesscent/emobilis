from django import forms
from .models import Doctor, Staff, OutPatientRecord, InPatientRecord, Patient

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'  # Includes all fields in the model
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class InPatientRecordForm(forms.ModelForm):
    class Meta:
        model = InPatientRecord
        fields = '__all__'
        widgets = {
            'reason_for_visit': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'sickness': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'diagnosis': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'medication': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'date_addmitted': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_discharged': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class OutPatientRecordForm(forms.ModelForm):
    class Meta:
        model = OutPatientRecord
        fields = '__all__'
        widgets = {
            'reason_for_visit': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'sickness': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'diagnosis': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'medication': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        }