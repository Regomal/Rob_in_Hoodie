from django import forms

from apps.blog.models import CommentArticle


class CommentFormLogin(forms.ModelForm):

    class Meta:
        model = CommentArticle
        fields = ['text', 'email', 'username', 'article', 'is_checked']
