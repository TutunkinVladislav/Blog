from django.conf.urls import url
from django.urls import path

from films import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^genre/(?P<id>\d+)$', views.page_genre, name='page_genre'),
    url(r'^posts/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='page_post'),
    path('search', views.search, name='search'),
]
