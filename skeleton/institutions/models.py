from django.db import models

# Create your models here.

class Institution(models.Model):
    name = models.CharField(max_length=100, default='')


class Doctor(models.Model):
    employee_id = models.IntegerField(unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(default='', max_length=10)
    phone_number = models.IntegerField()
    specialization = models.CharField(default='', max_length=20)
    department = models.CharField(default='', max_length=20)

    def __str__(self):
        return f'{self.user.username} Doctor Profile'

class Staff(models.Model):
    employee_id = models.IntegerField(unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(default='', max_length=10)
    phone_number = models.IntegerField()
    position = models.CharField(default='', max_length=20)
    department = models.CharField(default='', max_length=20)

    def __str__(self):
        return f'{self.user.username} Staff Profile'
        