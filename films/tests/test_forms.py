from django.test import TestCase

from films.forms import SearchForm, CreateCommentForm, CreateUserForm
from films.models import Comment, User


class SearchFormTest(TestCase):

    def test_query_placeholder(self):
        form = SearchForm()
        self.assertEquals(form.fields['query'].widget.attrs['placeholder'], 'Поиск...')


class CreateCommentFormTest(TestCase):

    def test_meta_model(self):
        form = CreateCommentForm()
        self.assertEquals(form._meta.model, Comment)

    def test_meta_fields(self):
        form = CreateCommentForm()
        self.assertEquals(form._meta.fields, ('name', 'email', 'text'))

    def test_meta_labels(self):
        form = CreateCommentForm()
        self.assertEquals(form._meta.labels, {'name': '', 'email': '', 'text': '', })

    def test_meta_widgets(self):
        form = CreateCommentForm()
        self.assertEquals(form._meta.widgets['name'].attrs['placeholder'], 'Имя')
        self.assertEquals(form._meta.widgets['name'].attrs['readonly'], 'readonly')
        self.assertEquals(form._meta.widgets['email'].attrs['placeholder'], 'Email')
        self.assertEquals(form._meta.widgets['email'].attrs['readonly'], 'readonly')
        self.assertEquals(form._meta.widgets['text'].attrs['placeholder'], 'Комментарий')


class CreateUserFormTest(TestCase):

    def test_field_name(self):
        form = CreateUserForm()
        self.assertEquals(form.fields['name'].label, '')
        self.assertEquals(form.fields['name'].max_length, 70)
        self.assertEquals(form.fields['name'].required, True)
        self.assertEquals(form.fields['name'].widget.attrs['placeholder'], 'Введите ваше имя')

    def test_field_email(self):
        form = CreateUserForm()
        self.assertEquals(form.fields['email'].label, '')
        self.assertEquals(form.fields['email'].max_length, 100)
        self.assertEquals(form.fields['email'].required, True)
        self.assertEquals(form.fields['email'].widget.attrs['placeholder'], 'Введите ваш email')

    def test_field_password(self):
        form = CreateUserForm()
        self.assertEquals(form.fields['password'].label, '')
        self.assertEquals(form.fields['password'].required, True)
        self.assertEquals(form.fields['password'].widget.attrs['placeholder'], 'Введите ваш пароль')

    def test_field_repeat_password(self):
        form = CreateUserForm()
        self.assertEquals(form.fields['repeat_password'].label, '')
        self.assertEquals(form.fields['repeat_password'].required, True)
        self.assertEquals(form.fields['repeat_password'].widget.attrs['placeholder'], 'Введите пароль ещё раз')

    def test_equal_passwords(self):
        data = {'name': 'Имя', 'email': 'email@mail.ru', 'password': 'password', 'repeat_password': 'password'}
        form = CreateUserForm(data=data)
        self.assertTrue(form.is_valid())

    def test_email_valid(self):
        data = {'name': 'Имя', 'email': 'email@mail.ru', 'password': 'password', 'repeat_password': 'password'}
        form = CreateUserForm(data=data)
        User.objects.create(
            username='username',
            email='email@mail.ru',
            first_name='first_name'
        )
        self.assertFalse(form.is_valid())
