from django import forms
from core.models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["name", "body"]
