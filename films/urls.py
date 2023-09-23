from django.urls import path

from films import views

urlpatterns = [
    path('', views.index, name='index'),
    path('genre/<slug:slug>', views.page_genre, name='page_genre'),
    path('posts/<slug:slug>', views.page_post, name='page_post'),
    path('search', views.search, name='search'),
    path('regist', views.regist, name='regist'),
    path('delete_comment', views.delete_comment, name='delete_comment'),
]
