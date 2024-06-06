from django.utils import timezone
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import User
from django.templatetags.static import static

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

      food_items = [
        {
            "name": "Shaker Salad",
            "description": "Salad bar that offers a vibrant selection of crisp greens, colorful veggies, and gourmet toppings, all ready to be mixed to your heart's content.",
            "image_url": static('images/food/shaker_salad.jpg')
        },
        {
            "name": "Curry On Indian Cuisine",
            "description": "Savor the authentic flavors of India with our delicious rice and curry dishes!",
            "image_url": static('images/food/curry.jpg')
        },
        {
            "name": "Fresh Fruit",
            "description": "Enjoy a healthy snack with our fresh, nutritious fruit bursting with natural goodness!",
            "image_url": static('images/food/freshfruit.jpg')
        },
    ]
      context['food_items'] = food_items
      
    return render(request, 'home/home.html', context)