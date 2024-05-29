import os
from django.conf import settings

def get_allergy_icon_dir():
    allergy_dir = os.path.join(settings.MEDIA_ROOT, 'allergy')
    os.makedirs(allergy_dir, exist_ok=True)
    return allergy_dir