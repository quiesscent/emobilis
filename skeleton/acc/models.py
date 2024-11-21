from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('institution', 'Institution'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    class Meta:
        verbose_name_plural ='Users'

    def __str__(self):
        return self.email

class DoctorProfile(models.Model):
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # employee_id = models.IntegerField(unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(default='', max_length=10)
    phone_number = models.IntegerField()
    specialization = models.CharField(default='', max_length=20)
    license_no = models.IntegerField()
    department = models.CharField(default='', max_length=20)
    profile = models.ImageField(upload_to='doctors/')

    def __str__(self):
        return f'{self.user.username} Doctor Profile'

class PatientProfile(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # patient_id = models.IntegerField(unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(default='', max_length=10)
    phone_number = models.IntegerField()
    adress = models.CharField(default='', max_length=20)
    emergency_contact_name = models.CharField(default='', max_length=20)
    emergency_contact_number = models.IntegerField(default='')
    profile = models.ImageField(upload_to='patients/')

    def __str__(self):
        return f'{self.patient.username} Patient Profile'

    