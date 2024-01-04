from django.forms import ModelForm

from .models import Note
from django import forms

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["note"]
        widgets = {
            "note": forms.Textarea(attrs={"class": "box"}),
        }
