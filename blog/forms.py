from django import forms
from .models import BlogPost, Comment
from django.forms import fields


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = 'title', 'content', 'image', 'category', 'status'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = 'name', 'body'

        widgets = {
            'Name': forms.TextInput(),
            'body': forms.Textarea()
        }
