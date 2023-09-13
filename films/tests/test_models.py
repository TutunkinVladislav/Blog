from django.core.exceptions import ValidationError
from django.test import TestCase

from films.models import User, Genre, Post


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            username = 'admin',
            email = 'admin@mail.ru',
            first_name = 'Администратор'
        )
        Genre.objects.create(
            title = 'Комедии',
            slug = 'comedy',
            image = 'images/example.jpg'
        )
        Post.objects.create(
            user = User.objects.get(id=1),
            genre = Genre.objects.get(id=1),
            title = 'Пост',
            slug = 'post',
            description = 'Описание',
            text = 'Текст',
            image = 'images/example.jpg',
            year = 2020,
            country = 'country',
            director = 'Режиссер',
            actors = 'Актеры',
            play = 100,
            date = '01.01.2020'
        )

    def test_user_verbose_name(self):
        obj = Post.objects.get(id=1)
        verbose_name = obj._meta.get_field('user').verbose_name
        self.assertEquals(verbose_name, 'Пользователь')

    def test_user_null(self):
        obj = Post.objects.get(id=1)
        null = obj._meta.get_field('user').null
        self.assertEquals(null, True)

    def test_genre_null(self):
        obj = Post.objects.get(id=1)
        self.assertTrue(obj._meta.get_field('genre').null)

    def test_genre_verbose_name(self):
        obj = Post.objects.get(id=1)
        verbose_name = obj._meta.get_field('genre').verbose_name
        self.assertEquals(verbose_name, 'Жанр')

    def test_field_title(self):
        obj = Post.objects.get(id=1)
        obj_meta = obj._meta.get_field('title')
        self.assertEquals(obj_meta.verbose_name, 'Заголовок')
        self.assertEquals(obj_meta.max_length, 250)
        self.assertTrue(obj_meta.unique)

    def test_field_slug(self):
        obj = Post.objects.get(id=1)
        obj_meta = obj._meta.get_field('slug')
        self.assertEquals(obj_meta.verbose_name, 'Псевдоним')
        self.assertEquals(obj_meta.max_length, 70)
        self.assertEquals(obj_meta.default, '')

    def test_field_description(self):
        obj = Post.objects.get(id=1)
        self.assertEquals(obj._meta.get_field('description').verbose_name, 'Описание')

    def test_field_text(self):
        obj = Post.objects.get(id=1)
        self.assertEquals(obj._meta.get_field('text').verbose_name, 'Текст')

    def test_field_image(self):
        obj = Post.objects.get(id=1)
        self.assertEquals(obj._meta.get_field('image').verbose_name, 'Изображение')
        self.assertEquals(obj._meta.get_field('image').upload_to, 'images')

    def test_field_year(self):
        obj = Post.objects.get(id=1)
        self.assertEquals(obj._meta.get_field('year').verbose_name, 'Год')
        obj.year = 1800
        self.assertRaises(ValidationError, obj.full_clean)
        obj.year = 2500
        self.assertRaises(ValidationError, obj.full_clean)

    def test_field_country(self):
        obj = Post.objects.get(id=1)
        self.assertEquals(obj._meta.get_field('country').verbose_name, 'Страна')
        self.assertEquals(obj._meta.get_field('country').max_length, 70)

    def test_field_director(self):
        obj = Post.objects.get(id=1)
        self.assertEquals(obj._meta.get_field('director').verbose_name, 'Режиссёр')
        self.assertEquals(obj._meta.get_field('director').max_length, 70)

    def test_field_director(self):
        obj = Post.objects.get(id=1)
        self.assertEquals(obj._meta.get_field('actors').verbose_name, 'Актёры')

    def test_field_play(self):
        obj = Post.objects.get(id=1)
        obj_meta = obj._meta.get_field('play')
        self.assertEquals(obj_meta.verbose_name, 'Продолжительность')
        self.assertEquals(obj_meta.help_text, 'В минутах')
        obj.play = 0
        self.assertRaises(ValidationError, obj.full_clean)
        obj.play = 250
        self.assertRaises(ValidationError, obj.full_clean)

    def test_field_date(self):
        obj = Post.objects.get(id=1)
        self.assertEquals(obj._meta.get_field('date').verbose_name, 'Дата добавления')
        self.assertTrue(obj._meta.get_field('date').auto_now_add)

    def test_meta_post(self):
        obj = Post.objects.get(id=1)
        self.assertEquals(obj._meta.ordering, ['-date'])
        self.assertEquals(obj._meta.verbose_name, 'Пост')
        self.assertEquals(obj._meta.verbose_name_plural, 'Посты')

    def test_play_minutes(self):
        obj = Post.objects.get(id=1)
        self.assertEquals(obj.play_minutes(), str(obj.play) + ' мин.')

    def test_str(self):
        obj = Post.objects.get(id=1)
        self.assertEquals(str(obj), f'{obj.title} ({obj.genre.title})')
