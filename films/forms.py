from django import forms
from django.core.exceptions import ValidationError

from films.models import Comment, User


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
            'name': forms.TextInput(attrs={
                'placeholder': 'Имя',
                'readonly': 'readonly'
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Email',
                'readonly': 'readonly'
            }),
            'text': forms.Textarea(attrs={'placeholder': 'Комментарий'}),
        }


class CreateUserForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=70,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя'})
    )
    email = forms.EmailField(
        label='',
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Введите ваш email'})
    )
    password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите ваш пароль'})
    )
    repeat_password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Введите пароль ещё раз'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')
        email = cleaned_data.get('email')
        if password != repeat_password:
            raise ValidationError('Пароли должны совпадать')
        if (User.objects.filter(email=email).exists()
                or User.objects.filter(username=email).exists()):
            raise ValidationError('Пользователь с таким email уже существует')
