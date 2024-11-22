from django.db import models
from tinymce import models as tinymce_models
from django.utils import timezone

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(default='', max_length=100)
    employee_id = models.IntegerField(unique=True) # autogenerated
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, default='')
    date_of_birth = models.DateField()
    gender = models.CharField(default='', max_length=10)
    phone_number = models.IntegerField()
    specialization = models.CharField(default='', max_length=20)
    department = models.CharField(default='', max_length=20)

    def __str__(self):
        return f'{self.name } Doctor Profile'

class Staff(models.Model):
    name = models.CharField(default='', max_length=100)
    employee_id = models.IntegerField(unique=True) # autogenerated
    date_of_birth = models.DateField()
    gender = models.CharField(default='', max_length=10)
    phone_number = models.IntegerField()
    position = models.CharField(default='', max_length=20)
    department = models.CharField(default='', max_length=20)

    def __str__(self):
        return f'{self.name} Staff Profile'
        
class Patient(models.Model):
    name = models.CharField(default='', max_length=100)
    patient_id = models.IntegerField(unique=True) # autogenerated
    age = models.IntegerField()
    date_of_birth = models.DateField()
    gender = models.CharField(default='', max_length=10)
    phone_number = models.IntegerField()

    def __str__(self):
        return f'{self.name} Patient Profile'

class InPatientRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='patient_id')
    record_id = models.IntegerField(unique=True, editable=False)
    reason_for_visit = tinymce_models.HTMLField(max_length=10000, default='')
    sickness = tinymce_models.HTMLField(max_length=10000, default='')
    diagnosis = tinymce_models.HTMLField(max_length=10000, default='')
    medication = tinymce_models.HTMLField(max_length=10000, default='')
    payment_method = models.CharField(default='', max_length=20)
    room_no = models.IntegerField(unique=True)
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    next_of_kin_name = models.CharField(default='', max_length=20)
    next_of_kin_contact = models.IntegerField()
    next_of_kin_address = models.IntegerField()
    date_addmitted = models.DateTimeField()
    date_discharged = models.DateTimeField()
    updated_at = models.DateTimeField(default=timezone.now)
    
    
    def save(self, *args, **kwargs):
        if not self.record_id:  # Only set if it doesn't already have a value
            # Get the last record_id or start from 1
            last_record = InPatientRecord.objects.order_by('-record_id').first()
            if last_record:
                self.record_id = last_record.record_id + 1
            else:
                self.record_id = 1
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.name } Inpatient Profile'

class OutPatientRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='patient_id')
    record_id = models.IntegerField(unique=True, editable=False)
    reason_for_visit = tinymce_models.HTMLField(max_length=10000, default='')
    sickness = tinymce_models.HTMLField(max_length=10000, default='')
    diagnosis = tinymce_models.HTMLField(max_length=10000, default='')
    medication = tinymce_models.HTMLField(max_length=10000, default='')
    payment_method = models.CharField(default='', max_length=20)
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, )
    next_of_kin_name = models.CharField(default='', max_length=20)
    next_of_kin_contact = models.IntegerField()
    next_of_kin_address = models.IntegerField()
    updated_at = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        if not self.record_id:  
            last_record = OutPatientRecord.objects.order_by('-record_id').first()
            if last_record:
                self.record_id = last_record.record_id + 1
            else:
                self.record_id = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} Outpatient Profile'

