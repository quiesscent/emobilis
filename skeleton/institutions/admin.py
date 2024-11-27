from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Staff)
admin.site.register(Patient)
admin.site.register(InPatientRecord)
admin.site.register(OutPatientRecord)
admin.site.register(doctorAppointment)
