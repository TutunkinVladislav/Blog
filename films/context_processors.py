import datetime

from films.forms import SearchForm
from films.models import Genre, Comment, Post


def add_genre(request):
    genres = Genre.objects.all()
    search_form = SearchForm()
    return {'genres': genres, 'search_form': search_form}


def add_comments(request):
    comments = Comment.objects.all().order_by('-id')[:3]
    return {'comments': comments}


def add_three_post(request):
    three_post = Post.objects.only('title').order_by('-date')[:3]
    return {'three_post': three_post}


def year(request):
    dt = datetime.datetime.now()
    return {'year': dt.year}
