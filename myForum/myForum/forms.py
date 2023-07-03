from django import forms
from .models import Topic, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Topic
        fields = ['subject', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'username',
            'placeholder': ('Username'),
            'name': 'username'  # Add name attribute
        }
    ))
    password = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
            'name': 'password'  # Add name attribute
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'username',
            'placeholder': ('Username'),
            'name': 'username'  # Add name attribute
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'type': 'email',
            'placeholder': ('Email'),
            'name': 'email'  # Add name attribute
        }
    ))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
            'name': 'password1'  # Add name attribute
        }
    ))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Repeat Password',
            'name': 'password2'  # Add name attribute
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'name': 'email'  # Add name attribute
        }
    ))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

