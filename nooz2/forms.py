from django import forms
from django.conf import settings
from .models import Post, Category, Comment

# MAX_POST_LENGTH = settings.MAX_POST_LENGTH

choices = Category.objects.all().values_list('name','name')
choices_list = []

for item in choices:
    choices_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'header_image', 'category', 'author', 'description', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'userid', 'type': 'hidden'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'description', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

    
    #def clean_content(self):
    #   content = self.cleaned_data.get("content")
    #  if len(content) > MAX_POST_LENGTH:
    #     raise forms.ValidationError("This message is too long")
    #return content


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'userid', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }