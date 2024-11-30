from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from patients.models import patientAppointment
from .models import Patient, MedicalReport
from acc.models import InstitutionDoctorProfile
from institutions.models import InPatientRecord, OutPatientRecord, doctorAppointment

@receiver(post_save, sender=patientAppointment)
def increment_appointment_count(sender, instance, created, **kwargs):
    if created:  # Only increment if a new appointment is created
        doctor = instance.doctor
        doctor.total_appointments += 1
        doctor.total_patients += 1
        doctor.save()

@receiver(post_delete, sender=patientAppointment)
def decrement_appointment_count(sender, instance, **kwargs):
    doctor = instance.doctor
    doctor.save()


@receiver(post_save, sender=Patient)
def increment_appointment_count(sender, instance, created, **kwargs):
    if created:  # Only increment if a new patient is created
        doctor = instance.doctor
        doctor.total_patients += 1
        doctor.save()

@receiver(post_delete, sender=Patient)
def decrement_appointment_count(sender, instance, **kwargs):
    doctor = instance.doctor
    doctor.save()


@receiver(post_save, sender=MedicalReport)
def increment_appointment_count(sender, instance, created, **kwargs):
    if created:  # Only increment if a new report is created
        doctor = instance.doctor
        doctor.total_reports += 1
        doctor.save()

@receiver(post_delete, sender=MedicalReport)
def decrement_appointment_count(sender, instance, **kwargs):
    doctor = instance.doctor
    doctor.save()


# Signal to update totals after saving an Appointment
@receiver(post_save, sender=doctorAppointment)
def update_total_appointments(sender, instance, **kwargs):
    doctor_profile = InstitutionDoctorProfile.objects.get(doctor=instance.doctor)
    doctor_profile.total_appointments += 1
    doctor_profile.save()


# Signal to update totals after deleting an Appointment
@receiver(post_delete, sender=doctorAppointment)
def decrease_total_appointments(sender, instance, **kwargs):
    doctor_profile = InstitutionDoctorProfile.objects.get(doctor=instance.doctor)
    doctor_profile.total_appointments -= 1
    doctor_profile.save()


# Signal to update total patients after saving a Patient
@receiver(post_save, sender=InPatientRecord)
def update_total_patients(sender, instance, **kwargs):
    doctor_profile = InstitutionDoctorProfile.objects.get(doctor=instance.assigned_doctor)
    doctor_profile.total_patients += 1
    doctor_profile.save()


# Signal to update total patients after deleting a Patient
@receiver(post_delete, sender=InPatientRecord)
def decrease_total_patients(sender, instance, **kwargs):
    doctor_profile = InstitutionDoctorProfile.objects.get(doctor=instance.assigned_doctor)
    doctor_profile.total_patients -= 1
    doctor_profile.save()

# Signal to update total patients after saving a Patient
@receiver(post_save, sender=OutPatientRecord)
def update_total_patients(sender, instance, **kwargs):
    doctor_profile = InstitutionDoctorProfile.objects.get(doctor=instance.assigned_doctor)
    doctor_profile.total_patients += 1
    doctor_profile.save()


# Signal to update total patients after deleting a Patient
@receiver(post_delete, sender=OutPatientRecord)
def decrease_total_patients(sender, instance, **kwargs):
    doctor_profile = InstitutionDoctorProfile.objects.get(doctor=instance.assigned_doctor)
    doctor_profile.total_patients -= 1
    doctor_profile.save()