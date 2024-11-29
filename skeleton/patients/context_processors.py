from acc.models import CustomUser, PatientProfile
from django.shortcuts import get_object_or_404
def profile_image(request):
    profile = None
    if request.user.is_authenticated:
        patient = get_object_or_404(CustomUser, id=request.user.id)
        user_profile = PatientProfile.objects.filter(patient=patient).first()
        
        if user_profile:
            profile = user_profile.profile

    return {'patient_profile': profile}