from django import forms
from django.conf import settings
from .models import Post

#MAX_POST_LENGTH = settings.MAX_POST_LENGTH


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'author', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

    
    #def clean_content(self):
    #   content = self.cleaned_data.get("content")
    #  if len(content) > MAX_POST_LENGTH:
    #     raise forms.ValidationError("This message is too long")
    #return content