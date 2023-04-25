from django import forms
from .models import Topic


class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Topic
        fields = ['subject', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
