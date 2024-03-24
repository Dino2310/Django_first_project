from django import forms
from .models import *
from django.contrib.auth.models import User

class FormSubUser(forms.ModelForm):
    photo = forms.ImageField()
    about = forms.CharField(widget=forms.Textarea(
        attrs={'class':'input', 'placeholder':'напишите о себе'}))
    
    class Meta:
        model = SubUser
        fields = ["photo", "about"]

class UserForm(forms.ModelForm):
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'input', 'placeholder':'Фамилия'}
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'input', 'placeholder':'имя'}
    ))
    email = forms.EmailInput()
    class Meta:
        model = User
        fields = ["last_name", "first_name", "email"]

    


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