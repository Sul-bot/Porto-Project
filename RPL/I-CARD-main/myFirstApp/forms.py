from django import forms
from .models import Image

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image', 'image_type')
        
