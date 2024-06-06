from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.templatetags.static import static

@login_required
def account(request):
    dietary_restrictions = [
        {
            "title": "Dairy",
            "image_url": static('images/allergy/dairy.png'),
            "is_selected": True
        },
        {
            "title": "Peanuts",
            "image_url": static('images/allergy/peanuts.png'),
            "is_selected": False
        },
        {
            "title": "Soy",
            "image_url": static('images/allergy/soy.png'),
            "is_selected": False
        },
        {
            "title": "Tree Nuts",
            "image_url": static('images/allergy/tree_nuts.png'),
            "is_selected": False
        },
        {
            "title": "Gluten",
            "image_url": static('images/allergy/wheat.png'),
            "is_selected": True
        },
        {
            "title": "Fish",
            "image_url": static('images/allergy/fish.png'),
            "is_selected": False
        },
    ]
    
    context = {
        'dietary_restrictions': dietary_restrictions
    }

    return render(request, 'account/account.html', context)