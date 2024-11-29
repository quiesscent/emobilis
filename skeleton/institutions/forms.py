from django import forms
from .models import Doctor, Staff, OutPatientRecord, InPatientRecord, Patient

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'  # Includes all fields in the model
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_id': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
        }

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_id': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'patient_id': forms.TextInput(attrs={'class': 'form-control'}),
        }

class InPatientRecordForm(forms.ModelForm):
    class Meta:
        model = InPatientRecord
        fields = '__all__'
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'reason_for_visit': forms.Textarea(attrs={'class': 'form-control'}),
            'sickness': forms.Textarea(attrs={'rows': '5', 'class': 'form-control'}),
            'diagnosis': forms.Textarea(attrs={'rows': '5','class': 'form-control'}),
            'medication': forms.Textarea(attrs={'rows': '5','class': 'form-control'}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control'}),
            'room_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'assigned_doctor': forms.Select(attrs={'class': 'form-control'}),
            'next_of_kin_name': forms.TextInput(attrs={'class': 'form-control'}),
            'next_of_kin_contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'record_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'next_of_kin_address': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_addmitted': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'updated_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'date_discharged': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
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
            'assigned_doctor': forms.Select(attrs={'class': 'form-control'}),
            'next_of_kin_name': forms.TextInput(attrs={'class': 'form-control'}),
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'next_of_kin_contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'next_of_kin_address': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control'}),
            'record_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'updated_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }