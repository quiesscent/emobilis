from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from acc.models import InstitutionProfile, InstitutionDoctorProfile
from .models import Doctor, Patient, Staff

# Signal to update total doctors when a doctor profile is saved
@receiver(post_save, sender=Doctor)
def increment_doctor_count(sender, instance, created, **kwargs):
    if created:  
        institution = InstitutionProfile.objects.get(institution=instance.institution)
        # Update the totals
        institution.total_doctors += 1
        institution.total_employees += 1
        institution.save()

@receiver(post_delete, sender=Doctor)
def decrement_doctor_count(sender, instance, **kwargs):
    institution = InstitutionProfile.objects.get(institution=instance.institution)
    # Decrement the totals
    if institution.total_doctors > 0:
        institution.total_doctors -= 1
    if institution.total_employees > 0:
        institution.total_employees -= 1
        # Save the changes
    institution.save()
    
@receiver(post_save, sender=Patient)
def increment_patient_count(sender, instance, created, **kwargs):
    if created:  
        institution = InstitutionProfile.objects.get(institution=instance.institution)
        # Update the totals
        institution.total_patients += 1
        institution.save()

@receiver(post_delete, sender=Patient)
def decrement_patient_count(sender, instance, **kwargs):
    institution = InstitutionProfile.objects.get(institution=instance.institution)
    # Decrement the totals
    if institution.total_patients > 0:
        institution.total_patients -= 1
        # Save the changes
    institution.save()
    
@receiver(post_save, sender=Staff)
def increment_staff_count(sender, instance, created, **kwargs):
    if created:  
        institution = InstitutionProfile.objects.get(institution=instance.institution)
        # Update the totals
        institution.total_staff += 1
        institution.total_employees += 1
        institution.save()

@receiver(post_delete, sender=Staff)
def decrement_staff_count(sender, instance, **kwargs):
    institution = InstitutionProfile.objects.get(institution=instance.institution)
    # Decrement the totals
    if institution.total_staff > 0:
        institution.total_staff -= 1
        # Save the changes
    if institution.total_employees > 0:
        institution.total_employees -= 1
        
    institution.save()