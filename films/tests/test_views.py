from django.test import TestCase, Client

from films.forms import CreateCommentForm
from films.models import User, Genre, Post, Comment


class IndexViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            username='admin',
            email='admin@mail.ru',
            first_name='Администратор'
        )
        Genre.objects.create(
            title='Комедии',
            slug='comedy',
            image='images/example.jpg'
        )
        Post.objects.create(
            user=User.objects.get(id=1),
            genre=Genre.objects.get(id=1),
            title='Пост',
            slug='post',
            description='Описание',
            text='Текст',
            image='images/example.jpg',
            year=2020,
            country='country',
            director='Режиссер',
            actors='Актеры',
            play=100,
            date='01.01.2020'
        )

    def test_page(self):
        response = self.client.get('/films/')
        self.assertEquals(response.status_code, 200)

    def test_template(self):
        response = self.client.get('/films/')
        self.assertTemplateUsed(response, 'index.html')

    def test_context(self):
        response = self.client.get('/films/')
        self.assertTrue(response.context['films'])

    def test_content(self):
        response = self.client.get('/films/')
        self.assertEquals(response.context['films'].get(), Post.objects.get(id=1))


class PageGenreViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            username='admin',
            email='admin@mail.ru',
            first_name='Администратор'
        )
        Genre.objects.create(
            title='Комедии',
            slug='comedy',
            image='images/example.jpg'
        )
        Post.objects.create(
            user=User.objects.get(id=1),
            genre=Genre.objects.get(id=1),
            title='Пост',
            slug='post',
            description='Описание',
            text='Текст',
            image='images/example.jpg',
            year=2020,
            country='country',
            director='Режиссер',
            actors='Актеры',
            play=100,
            date='01.01.2020'
        )
        Comment.objects.create(
            film=Post.objects.get(id=1),
            name='Имя',
            email='Email',
            text='Текст',
            date='01.01.2020'
        )

    def test_page(self):
        response = self.client.get('/films/genre/comedy')
        self.assertEquals(response.status_code, 200)

    def test_template(self):
        response = self.client.get('/films/genre/comedy')
        self.assertTemplateUsed(response, 'posts.html')

    def test_context(self):
        response = self.client.get('/films/genre/comedy')
        self.assertTrue(response.context['posts'])
        self.assertTrue(response.context['obj'])
        self.assertTrue(response.context['genre_comments'])
        self.assertTrue(response.context['films'])

    def test_content(self):
        response = self.client.get('/films/genre/comedy')
        self.assertEquals(response.context['obj'], Genre.objects.get(slug='comedy'))
        self.assertEquals(response.context['posts'].get(), Post.objects.get())
        self.assertEquals(response.context['genre_comments'], Comment.objects.all().count())
        self.assertEquals(response.context['films'].get(), Post.objects.get())


class PagePostViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            username='admin',
            email='admin@mail.ru',
            first_name='Администратор'
        )
        Genre.objects.create(
            title='Комедии',
            slug='comedy',
            image='images/example.jpg'
        )
        Post.objects.create(
            user=User.objects.get(id=1),
            genre=Genre.objects.get(id=1),
            title='Пост',
            slug='post',
            description='Описание',
            text='Текст',
            image='images/example.jpg',
            year=2020,
            country='country',
            director='Режиссер',
            actors='Актеры',
            play=100,
            date='01.01.2020'
        )
        Comment.objects.create(
            film=Post.objects.get(id=1),
            name='Имя',
            email='Email',
            text='Текст',
            date='01.01.2020'
        )

    def test_page(self):
        response = self.client.get('/films/posts/post')
        self.assertEquals(response.status_code, 200)

    def test_template(self):
        response = self.client.get('/films/posts/post')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_context(self):
        response = self.client.get('/films/posts/post')
        self.assertTrue(response.context['post'])
        self.assertTrue(response.context['form'])
        self.assertTrue(response.context['post_comments'])
        self.assertTrue(response.context['films'])

    def test_content(self):
        response = self.client.get('/films/posts/post')
        # initial = {'name': 'Администратор', 'email': 'admin@mail.ru'}
        # self.assertEquals(response.context['form'], CreateCommentForm(initial=initial))
        self.assertEquals(response.context['post'], Post.objects.get(slug='post'))
        self.assertEquals(response.context['post_comments'].get(), Comment.objects.get())
        self.assertEquals(response.context['films'].get(), Post.objects.get())