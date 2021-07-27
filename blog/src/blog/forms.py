from django import forms
from django.forms import ModelForm

from .models import Feedback


class FeedBackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        exclude = ('id',)
        widgets = {
            'Имя': forms.TextInput(),
            'Email': forms.EmailInput(),
            'Сообщение': forms.Textarea(),
        }
