from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.urls import reverse

from films.forms import SearchForm, CreateCommentForm, CreateUserForm
from films.models import Genre, Post, Comment, User


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


def page_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post_comments = Comment.objects.filter(film__exact=post)
    films = Post.objects.all().order_by('-date')[:9]
    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.name = request.user.first_name
            comment.email = request.user.email
            comment.film = post
            comment.save()
            return redirect('page_post', pk=post.pk)
    else:
        form = CreateCommentForm()
    context = {
        'post': post, 'post_comments': post_comments,
        'films': films, 'form': form
    }
    return render(request, 'post_detail.html', context=context)


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


def regist(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(email, email, password)
            user.first_name = name
            group = Group.objects.get(name='Авторы')
            user.groups.add(group)
            user.save()
            success = True

            # Отправка письма
            text = get_template('email/success_regist.html')
            html = get_template('email/success_regist.html')
            context = {'name': name}
            subject = 'Регистрация'
            from_email = 'admin@blogfilms.ru'
            text_content = text.render(context)
            html_content = html.render(context)
            message = EmailMultiAlternatives(subject, text_content, from_email, [email])
            message.attach_alternative(html_content, 'text/html')
            message.send()

            return render(request, 'regist.html', {'success': success})
    else:
        form = CreateUserForm()
    return render(request, 'regist.html', {'form': form})


@permission_required('films.can_delete_comment')
def delete_comment(request):
    comments = Comment.objects.all()
    for comment in comments:
        if comment.email == request.user.email:
            comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
