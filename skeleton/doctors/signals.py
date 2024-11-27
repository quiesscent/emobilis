from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from patients.models import patientAppointment
from .models import Patient, MedicalReport

@receiver(post_save, sender=patientAppointment)
def increment_appointment_count(sender, instance, created, **kwargs):
    if created:  # Only increment if a new appointment is created
        instance.doctor.total_appointments += 1
        instance.doctor.total_patients += 1
        instance.doctor.save()

@receiver(post_delete, sender=patientAppointment)
def decrement_appointment_count(sender, instance, **kwargs):
    instance.doctor.save()


@receiver(post_save, sender=Patient)
def increment_appointment_count(sender, instance, created, **kwargs):
    if created:  # Only increment if a new patient is created
        instance.doctor.total_patients += 1
        instance.doctor.save()

@receiver(post_delete, sender=Patient)
def decrement_appointment_count(sender, instance, **kwargs):
    instance.doctor.save()


@receiver(post_save, sender=MedicalReport)
def increment_appointment_count(sender, instance, created, **kwargs):
    if created:  # Only increment if a new report is created
        instance.doctor.total_reports += 1
        instance.doctor.save()

@receiver(post_delete, sender=MedicalReport)
def decrement_appointment_count(sender, instance, **kwargs):
    instance.doctor.save()
