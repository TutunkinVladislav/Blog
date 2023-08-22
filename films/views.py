from django.shortcuts import render

from films.models import Genre, Post


def index(request):
    genres = Genre.objects.all()
    films = Post.objects.all()
    context = {'genres': genres, 'films': films}
    return render(request, 'index.html', context=context)
