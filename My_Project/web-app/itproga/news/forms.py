from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'date']
        widgets = {
            'title': TextInput(attrs={'class ': 'form-control',
                                      'placeholder': 'Logo'}),
            'anons': TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Anons'}),
            'full_text': Textarea(attrs={'class': 'form-control',
                                         'placeholder': 'Text'}),
            'date': DateTimeInput(attrs={'type': 'date', 'placeholder': 'Date'})
        }
