from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.templatetags.static import static

@login_required
def favorites(request):
    food_items = [
        {
            "name": "Fire & Slice Pizza",
            "description": "Satisfy your cravings with a fresh, mouth-watering slice of pizza!",
            "image_url": static('images/food/pizza.jpg')
        },
        {
            "name": "The Pastry Kitchen",
            "description": "Treat yourself to indulgent brownies and delightful pastry goods, perfect for any sweet tooth!",
            "image_url": static('images/food/brownies.jpg')
        },
    ]
    
    context = {
        'food_items': food_items
    }
    
    return render(request, 'favorites/favorites.html', context)
