from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from films.forms import SearchForm, CreateCommentForm
from films.models import Genre, Post, Comment


def index(request):
    films = Post.objects.all().order_by('-date')
    context = {'films': films}
    return render(request, 'index.html', context=context)


def page_genre(request, id):
    obj = get_object_or_404(Genre, pk=id)
    posts = Post.objects.filter(genre__exact=obj).order_by('-date')
    genre_comments = Comment.objects.filter(film__exact=posts[:1]).count()
    films = Post.objects.all().order_by('-date')[:9]
    context = {'posts': posts, 'obj': obj, 'genre_comments': genre_comments, 'films': films}
    return render(request, 'posts.html', context=context)


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['post_comments'] = Comment.objects.filter(film__exact=self.get_object())
        context['films'] = Post.objects.all().order_by('-date')[:9]
        return context


def handler404(request, exception):
    return render(request, '404.html', status=404)


def search(request):
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        query = search_form.cleaned_data['query']
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query) |
            Q(year__icontains=query) | Q(country__icontains=query) |
            Q(director__icontains=query) | Q(actors__icontains=query)
        )
        page = request.GET.get('page', 1)
        paginator = Paginator(posts, 3)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        films = Post.objects.all().order_by('-date')[:9]
        genre_comments = ''
        context = {'posts': posts, 'query': query, 'films': films, 'genre_comments': genre_comments}
        return render(request, 'search.html', context=context)

# def create_comment(request):
#     form = CreateCommentForm()
#     return render(request, 'films/post_detail.html', {'form': form})