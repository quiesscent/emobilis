from django.db import models
from acc.models import CustomUser


# Create your models here.
class patientAppointment(models.Model):
    # Patient Information
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15)  # Adjust length for international numbers
    patient = models.CharField(max_length=100, default='')
    # Appointment Details
    preferred_appointment_date = models.DateField()
    preferred_time = models.CharField(
        max_length=20,
        choices=[
            ('Morning', 'Morning'),
            ('Afternoon', 'Afternoon'),
            ('Evening', 'Evening')
        ],
        default='Morning'
    )
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'doctor'})
    reason_for_visit = models.TextField()
    symptoms = models.TextField(blank=True, null=True)  # Optional field
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_relationship = models.CharField(max_length=50)
    emergency_contact_number = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_at'] 
    
    def __str__(self):
        return f'{self.full_name} Appointment'