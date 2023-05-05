from .models import *
from django import forms
from django.forms import ModelForm
from django.forms import TextInput, DateInput, EmailInput


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['name', 'last_name', 'job', 'date_of_dirth', 'phone', 'email']


class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ['model', 'number']


class AnketaForm(forms.ModelForm):
    class Meta:
        model = Anketa
        fields = ['number1', 'number2', 'number3', 'number4', 'number5']

class OprosForm(forms.ModelForm, forms.Form):
    class Meta:
        model = Opros
        fields = ['text']