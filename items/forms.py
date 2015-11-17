from django import forms

from .models import List_items

class PostForm(forms.ModelForm):

    class Meta:
        model = List_items
        fields = ('title', 'address',)
