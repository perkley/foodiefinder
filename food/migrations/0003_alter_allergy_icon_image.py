# Generated by Django 5.0.6 on 2024-05-29 16:37

import django.core.files.storage
import food.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_alter_allergy_options_alter_allergy_icon_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergy',
            name='icon_image',
            field=models.ImageField(help_text='Upload 20x20 pixel image icon.', storage=django.core.files.storage.FileSystemStorage(base_url='/media/allergy/', location='D:\\MyFiles\\django\\foodiefinder\\media\\allergy'), upload_to=food.models.RenameUpload(), verbose_name='Allergy Icon Image'),
        ),
    ]
