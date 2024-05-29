from django import forms
from .models import Allergy


class AllergyAdminForm(forms.ModelForm):
    class Meta:
        model = Allergy
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AllergyAdminForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            if self.instance.icon_image:
                self.fields['icon_image'].help_text = self.instance.image_tag()