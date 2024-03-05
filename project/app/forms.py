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
    image = forms.ImageField(label="Картинки для поста", widget=forms.FileInput(
        attrs={'multiple':True}
    ))
    class Meta:
        model = Photo
        field = ['image']