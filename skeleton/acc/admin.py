from django.contrib import admin
from .models import CustomUser, DoctorProfile, InstitutionDoctorProfile, InstitutionProfile, PatientProfile
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(DoctorProfile)
admin.site.register(InstitutionDoctorProfile)
admin.site.register(InstitutionProfile)
admin.site.register(PatientProfile)




