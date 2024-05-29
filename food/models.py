import os
from django.db import models
from django.utils.deconstruct import deconstructible
from uuid import uuid4
from django.core.files.storage import FileSystemStorage
from food.utils import get_allergy_icon_dir
from django.conf import settings
from django.utils.html import mark_safe

@deconstructible
class RenameUpload(object):
    # Needed this out here so I could do the migration
    def __call__(self, instance, filename):
        ext = os.path.splitext(filename)[1]
    
        # set filename as random string
        filename = f'{uuid4().hex}{ext}'

        return filename

rename_upload = RenameUpload()


class Allergy(models.Model):
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Allergies'

    upload_storage = FileSystemStorage(location=get_allergy_icon_dir(), base_url=f'{settings.MEDIA_URL}allergy/')
    title = models.CharField(max_length=75)
    icon_image = models.ImageField(upload_to=rename_upload, verbose_name='Allergy Icon Image', help_text='Upload 20x20 pixel image icon.', storage=upload_storage)

    def image_tag(self):
        if self.icon_image:
            return mark_safe(f'<img src="{self.icon_image.url}" width="20" height=auto />')
        return "No Image"
    
    image_tag.short_description = 'Icon Image'

    def __str__(self):
        return self.title
    