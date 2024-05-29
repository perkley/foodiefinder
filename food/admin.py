from django.contrib import admin
from .models import Allergy
from .forms import AllergyAdminForm

class AllergyAdmin(admin.ModelAdmin):
    form = AllergyAdminForm
    search_fields = ("title",)
    ordering = ('title',)
    fields = ('title', 'icon_image',)
    list_display = ('title', 'image_tag',)
    
admin.site.register(Allergy, AllergyAdmin)


