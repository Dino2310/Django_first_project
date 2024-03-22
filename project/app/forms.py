from django import forms
from .models import *

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class':'input', 'placeholder':'название поста'}
    ))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class':'input', 'placeholder':'описание поста'}
    ))
    slug = forms.CharField(widget=forms.TextInput(
        attrs={'class':'input', 'placeholder':'Slug поста'}
    ))
    is_allowed  = forms.BooleanField(required=False)


    class Meta:
        fields = ['title', 'content', 'slug', "is_allowed"]
        model = Post

class ImageForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']
        widgets = {
            'image' : forms.ImageField()
            }
        
class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(
        attrs={'class':'input', 'placeholder':'добавьте комментарий...', 'id':'coment_in'}
    ))
    class Meta:
        fields = ["body"]
        model = Comments