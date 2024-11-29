import random
import string
from .models import Patient, Staff, Doctor, InPatientRecord, OutPatientRecord

def generate_patient_id():
   characters = string.ascii_uppercase + string.digits
   
   while True:
        
        random_code = ''.join(random.choices(characters, k=6))
        
        if not Patient.objects.filter(patient_id=random_code).exists():
            return random_code


def generate_staff_id():
    characters = string.ascii_uppercase + string.digits
   
    while True:
        
        random_code = ''.join(random.choices(characters, k=6))
    
        if not Staff.objects.filter(employee_id=random_code).exists():
            return random_code


def generate_doctor_id():
    characters = string.ascii_uppercase + string.digits
   
    while True:
        
        random_code = ''.join(random.choices(characters, k=6))
        
        if not Doctor.objects.filter(employee_id=random_code).exists():
            return random_code

def generate_inpatient_record_id():
    characters = string.digits
   
    while True:
        
        random_code = ''.join(random.choices(characters, k=6))
        
        if not InPatientRecord.objects.filter(record_id=random_code).exists():
            return random_code

def generate_outpatient_record_id():
    characters = string.digits

    while True:
        
        random_code = ''.join(random.choices(characters, k=6))
        
        if not OutPatientRecord.objects.filter(record_id=random_code).exists():
            return random_code