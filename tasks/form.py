from django import forms
from django.forms import ModelForm

from .models import tasksdb

class tasksform(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    
    class Meta: # here in 'Meta' M should be in capital letter.
        model = tasksdb
        fields = '__all__'
