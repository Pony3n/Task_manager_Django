from .models import Task, User
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

class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['nick', 'email', 'password']
        widgets = {
            'nick': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ник нэйм'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'password': TextInput(attrs={
                'type': 'password',
                'class': 'form-control',
                'placeholder': 'Password'

            })
        }

