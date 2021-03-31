from django import forms
from django.db.models import fields
from lolz2.models import Login, Result


class Form_one(forms.ModelForm):
    pwd = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('name', 'mail', 'pwd')


class Form_two(forms.ModelForm):
    class Meta:
        model = Result
        fields = '__all__'
