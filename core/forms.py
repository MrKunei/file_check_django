from django import forms
from .models import File


class FileCreateForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ('file',)
