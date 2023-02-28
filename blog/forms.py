from django import forms

from .models import Comment, Image

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "body")
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("title", "image")
