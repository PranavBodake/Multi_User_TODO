from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import TODO

class TODOForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'status']



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].label = ''
            self.fields[field_name].widget.attrs['class'] = 'hidden'  

        self.fields['username'].widget.attrs['placeholder'] = ''