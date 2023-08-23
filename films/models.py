import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()


class Genre(models.Model):
    """Модель жанров"""
    title = models.CharField(
        max_length=70,
        unique=True,
        verbose_name='Жанр',
        help_text='Введите название жанра'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='images'
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель постов"""
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.SET_NULL,
        null=True
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Жанр',
        related_name='genre'
    )
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=250,
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='images'
    )
    year = models.IntegerField(
        verbose_name='Год',
        validators=[MinValueValidator(1900), MaxValueValidator(datetime.date.today().year)]
    )
    country = models.CharField(
        verbose_name='Страна',
        max_length=70
    )
    director = models.CharField(
        verbose_name='Режиссёр',
        max_length=70
    )
    actors = models.TextField(
        verbose_name='Актёры'
    )
    play = models.IntegerField(
        verbose_name='Продолжительность',
        help_text='В минутах',
        validators=[MinValueValidator(1), MaxValueValidator(210)]
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )

    class Meta:
        ordering = ['-date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def play_minutes(self):
        return str(self.play) + ' мин.'

    play_minutes.short_description = 'Продолжительность'

    def __str__(self):
        return f'{self.title} ({self.genre.title})'


class Comment(models.Model):
    """Модель комментариев"""
    film = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='comments',
        verbose_name='Фильм'
    )
    name = models.CharField(
        verbose_name='Имя',
        max_length=70
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=254
    )
    text = models.TextField(
        verbose_name='Комментарий'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.name}: {self.text}'
