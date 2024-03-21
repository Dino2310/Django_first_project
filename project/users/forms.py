from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2']
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input', 'placeholder':"Введите имя"})
        self.fields['password1'].widget.attrs.update({'class': 'input', 'placeholder':"Введите пароль"})
        self.fields['password2'].widget.attrs.update({'class': 'input', 'placeholder':"Введите повторите пароль"})



class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.Textarea(
        attrs={'class':'input', 'placeholder':'введите логин'}
    ))
    password = forms.CharField(widget = forms.PasswordInput(
        attrs={'class':'input', 'placeholder':'введите пароль'}
    ))
    class Meta:
        model = User
        fields = ['username', 'password']
        