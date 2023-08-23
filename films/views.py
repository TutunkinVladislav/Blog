from django.shortcuts import render, get_object_or_404
from django.views import generic

from films.models import Genre, Post, Comment


def index(request):
    films = Post.objects.all().order_by('-date')
    context = {'films': films}
    return render(request, 'index.html', context=context)


def page_genre(request, id):
    obj = get_object_or_404(Genre, pk=id)
    posts = Post.objects.filter(genre__exact=obj).order_by('-date')
    genre_comments = Comment.objects.filter(film__exact=posts[:1]).count()
    context = {'posts': posts, 'obj': obj, 'genre_comments': genre_comments}
    return render(request, 'posts.html', context=context)


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['post_comments'] = Comment.objects.filter(film__exact=self.get_object())
        return context
