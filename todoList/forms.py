from django import forms
from .models import Todo

class TodoCreateForm(forms.ModelForm):
    class Meta :
        model = Todo
        exclude = ('to_prolong',)