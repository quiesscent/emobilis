from acc.models import DoctorProfile, CustomUser
from django.shortcuts import get_object_or_404
def profile_image(request):
    profile = None
    if request.user.is_authenticated:
        doctor = get_object_or_404(CustomUser, id=request.user.id)
        user_profile = DoctorProfile.objects.filter(doctor=doctor).first()
        if user_profile:
            profile = user_profile.profile
        
    return {'doc_profile': profile }