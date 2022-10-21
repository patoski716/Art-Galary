from django.forms import ModelForm
from django import forms
from .models import *

class CommentForm(ModelForm):
    name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={
        'class' : 'input', 'placeholder' :'Your name'
    }))
    
    body = forms.CharField(max_length=100,widget=forms.Textarea(attrs={
        'class' : 'input', 'placeholder' :'Comment Here', 'rows' : 3
    }))
    class Meta:
        model = Comment
        fields = ['name','body']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'