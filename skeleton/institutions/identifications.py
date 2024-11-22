import random
import string
from .models import Patient, Staff, Doctor

def generate_patient_id():
   characters = string.ascii_letters + string.digits
   
   while True:
        
        random_code = ''.join(random.choices(characters, k=6))
        
        if not Patient.objects.filter(patient_id=random_code).exists():
            return random_code


def generate_staff_id():
   characters = string.ascii_letters + string.digits
   
   while True:
        
        random_code = ''.join(random.choices(characters, k=6))
    
        if not Staff.objects.filter(employee_id=random_code).exists():
            return random_code


def generate_doctor_id():
   characters = string.ascii_letters + string.digits
   
   while True:
        
        random_code = ''.join(random.choices(characters, k=6))
        
        if not Doctor.objects.filter(employee_id=random_code).exists():
            return random_code
