from django.contrib import admin

from films.models import Genre, Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'genre', 'title', 'slug',
        'year', 'country', 'director',
        'actors', 'play_minutes', 'date'
    )
    list_per_page = 10
    search_fields = ('title', 'director', 'actors')
    date_hierarchy = 'date'
    list_filter = ('genre',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('film', 'name', 'text', 'date')
    list_per_page = 10


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'count_films')

    def count_films(self, obj):
        return obj.genre.count()

    count_films.short_description = 'Количество фильмов'
