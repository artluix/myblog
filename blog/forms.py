from django import forms
from .models import Post, Comment, Category


class PostForm(forms.Form):
    category = forms.CharField(50)
    title = forms.CharField(50)
    text = forms.CharField(widget=forms.Textarea())


    def save(self, user):
        data = self.cleaned_data
        category, created = Category.objects.get_or_create(title=data['category'])
        if created:
            category.save()
        post = Post.objects.create(author=user,
                                    title=data['title'],
                                    text=data['text'],
                                    category = category)
        return post


class CommentForm(forms.Form):
    author = forms.CharField(50, widget = forms.TextInput(attrs={'readonly': 'readonly'}))
    text = forms.CharField(widget=forms.Textarea())


    def save(self, post, user):
        data = self.cleaned_data
        comment = Comment.objects.create(author=user, post=post,
                                    text=data['text'])
        return comment
