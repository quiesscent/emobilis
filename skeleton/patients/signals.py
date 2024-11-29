from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from patients.models import patientAppointment

@receiver(post_save, sender=patientAppointment)
def increment_appointment_count(sender, instance, created, **kwargs):
    if created:  # Only increment if a new appointment is created
        # doctor = instance.doctor
        # doctor.total_appointments += 1
        # doctor.total_patients += 1
        # doctor.save()
        pass

@receiver(post_delete, sender=patientAppointment)
def decrement_appointment_count(sender, instance, **kwargs):
    # doctor = instance.doctor
    # doctor.save() 
    pass
