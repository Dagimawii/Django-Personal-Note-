from django import forms
from django.contrib.auth.models import User
from . models import Personal

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confrim = cleaned_data.get('password_confirm')

        if password and password_confrim and password != password_confrim:
            raise forms.ValidationError("passwords don't match ")
        return cleaned_data


class NoteForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['title', 'text']

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Note title'}),
            'text' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'note ' }),
        }


