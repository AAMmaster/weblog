from django import forms
from . models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'user_email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
