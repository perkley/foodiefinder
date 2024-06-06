import os
from django.db import models
from django.utils.deconstruct import deconstructible
from uuid import uuid4
from django.core.files.storage import FileSystemStorage
from food.utils import get_allergy_icon_dir
from django.conf import settings
from django.utils.html import mark_safe
from storages.backends.s3boto3 import S3Boto3Storage

@deconstructible
class RenameUpload(object):
    # Needed this out here so I could do the migration
    def __call__(self, instance, filename):
        ext = os.path.splitext(filename)[1]
    
        # set filename as random string
        filename = f'{uuid4().hex}{ext}'

        return filename

rename_upload = RenameUpload()

class AllergyMediaStorage(S3Boto3Storage):
        location = 'media/allergy'

class Allergy(models.Model):
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Allergies'    

    def get_storage():
        if settings.ENVIRONMENT == 'production':
            # Use S3Boto3Storage for production (assuming settings are configured)
            return AllergyMediaStorage()
        else:
            # Use FileSystemStorage for local development
            return FileSystemStorage(location=get_allergy_icon_dir(), base_url=f'{settings.MEDIA_URL}allergy/')
    
    upload_storage = get_storage() #FileSystemStorage(location=get_allergy_icon_dir(), base_url=f'{settings.MEDIA_URL}allergy/')
    title = models.CharField(max_length=75)
    icon_image = models.ImageField(upload_to=rename_upload, verbose_name='Allergy Icon Image', help_text='Upload 20x20 pixel image icon.', storage=upload_storage)

    def image_tag(self):
        if self.icon_image:
            return mark_safe(f'<img src="{self.icon_image.url}" width="20" height=auto />')
        return "No Image"
    
    image_tag.short_description = 'Icon Image'

    def __str__(self):
        return self.title
    