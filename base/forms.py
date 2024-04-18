from typing import Any
from django import forms
from .models import Article, Resource, Question, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'content']
        # widgets = {
        #     'content': forms.Textarea(attrs={'rows': 10}),
        # }
    
    # def clean_image(self):
    #     image = self.cleaned_data['image']
    #     return image


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'link']
        exclude = ['content']
        labels = {
            'link': 'Resource Link',
        }
    
    def clean_link(self):
        link = self.cleaned_data['link']
        return link
    

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'image', 'content']

    # def clean_image(self):
    #     image = self.cleaned_data['image']
    #     return image

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body',]
