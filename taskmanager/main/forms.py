from .models import Task
from django.forms import ModelForm, TextInput, DateInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'until']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название задачи'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание задачи'
            }),
            'until': DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        }
