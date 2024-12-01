from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from patients.models import patientAppointment
from acc.models import PatientProfile

@receiver(post_save, sender=patientAppointment)
def increment_appointment_count(sender, instance, created, **kwargs):
    if created:  
        patient = PatientProfile.objects.get(patient=instance.patient)
        # Update the totals
        patient.total_appointments += 1
        patient.total_visits += 1
        patient.save()

@receiver(post_delete, sender=patientAppointment)
def decrement_appointment_count(sender, instance, **kwargs):
    patient = PatientProfile.objects.get(patient=instance.patient)
    patient.save()
