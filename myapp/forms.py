from django import forms
from django.forms import ModelForm
from .models import Stories

class StoryForm(ModelForm):
    guest_check = forms.CharField(
        required=False,
        label="Type 'Enter' to confirm you're not a bot",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Type 'Enter' here"})
    )
    
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

    def clean_content(self):
        content = self.cleaned_data.get('content')
        word_count = len(content.split())
        if word_count > 500:
            raise forms.ValidationError("The story is more than 500 words. Please shorten your story.")
        return content

    def __init__(self, *args, **kwargs):
        self.user_authenticated = kwargs.pop('user_authenticated', False)
        super().__init__(*args, **kwargs)
        if self.user_authenticated:
            self.fields.pop('guest_check')  

    def clean_guest_check(self):
        if not self.user_authenticated:
            guest_check = self.cleaned_data.get('guest_check')
            if guest_check != 'Enter':
                raise forms.ValidationError("You must type 'Enter' to confirm you're not a bot.")
        return self.cleaned_data.get('guest_check')
        