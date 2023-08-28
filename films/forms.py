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
