from django.contrib import admin
from .models import Allergy
from django.utils.html import mark_safe
from django.conf import settings

class AllergyAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    ordering = ('title',)
    readonly_fields = ['icon_image']
    fields = ('icon_image', 'title')

    def icon_image(self, obj):
        return mark_safe(f'<img src="{settings.MEDIA_URL}allergy/{str(obj.icon_image)}" width="10" height=auto />')

    def get_fields(self, request, obj=None):
        fields = list(super().get_fields(request, obj=obj))
        if obj is None:
            fields.remove("icon_image")
        else: 
            print(obj.icon_image)

        return fields
    
admin.site.register(Allergy, AllergyAdmin)


