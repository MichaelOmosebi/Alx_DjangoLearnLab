from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'}),
        }

class TagWidget(forms.TextInput):
    template_name = 'blog/widgets/tag_widget.html'

    class Media:
        css = ('blog/css/tag_widget.css',)
        js = ('blog/js/tag_widget.js',)
