from django.utils import timezone
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    context = {
        'environment': settings.ENVIRONMENT
    }

    if request.user.is_authenticated:
      user = request.user

      # Check if the user is newly created
      is_new_user = user.date_joined.date() == timezone.now().date()  # Adjust logic if needed

      context['is_new_user'] = is_new_user
      context['t_date_joined'] = user.date_joined.date()
      context['t_now'] = timezone.now().date()
      
    return render(request, 'home/home.html', context)