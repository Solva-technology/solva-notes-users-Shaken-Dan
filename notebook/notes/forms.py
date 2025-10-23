from django import forms
from .models import Note

class AddNote(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('text', 'status', 'categories')
        labels = {
            'text': 'Текст',
            'status': 'Статус',
            'categories': 'Категории',
            'author': 'Автор'
        }
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'wide-input',
                'placeholder': 'Введите текст заметки'
            }),
            'status': forms.RadioSelect(),
            'categories': forms.CheckboxSelectMultiple(),
        }
