from .models import InstitutionProfile
import random
import string

def generate_institution_id():
    characters = string.ascii_uppercase + string.digits
   
    while True:
        
        random_code = ''.join(random.choices(characters, k=6))
    
        if not InstitutionProfile.objects.filter(registration_number=random_code).exists():
            return random_code
        