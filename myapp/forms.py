from django import forms
from django.forms import ModelForm
from .models import Stories

class StoryForm(ModelForm):
    class Meta:
        model = Stories
        fields = ['title', 'author', 'content', 'genre', 'isPublic']

        labels = {
            'title': '',
            'author': '',
            'content': '',
            'genre': '',
            'isPublic': 'Is it Public?',
        }
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter story title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter story content'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter story genre'}),
            'isPublic': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }