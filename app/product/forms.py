from django import forms

from .models import Comment

class SearchForm(forms.Form):
    q = forms.CharField(max_length=100)
    catid = forms.IntegerField()

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment', 'rating',]
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'input ', 'placeholder': 'Your review'}),
        }