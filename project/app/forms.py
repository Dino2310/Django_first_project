from django import forms
from .models import *

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class':'input', 'placeholder':'название поста'}
    ))
    contetn = forms.CharField(widget=forms.Textarea(
        attrs={'class':'input', 'placeholder':'описание поста'}
    ))
    slug = forms.CharField(widget=forms.TextInput(
        attrs={'class':'input', 'placeholder':'Slug поста'}
    ))

    class Meta:
        fields = ['title', 'content', 'slug']
        model = Post

class ImageForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']
        widgets = {
            'image' : forms.ImageField()
            }