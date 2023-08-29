from django import forms

from films.models import Comment


class SearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Поиск...'}
        )
    )


class CreateCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'text')
        labels = {
            'name': '',
            'email': '',
            'text': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'text': forms.Textarea(attrs={'placeholder': 'Комментарий'}),
        }
