from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (PostsList, PostDetail, SearchPosts,
                    ArticleCreate, ArticleUpdate, ArticleDelete,
                    NewsCreate, NewsUpdate, NewsDelete,
                    news_redirect,
                    CategoryListView, subscriptions, upgrade_me, subscribe )

from .views import new_add
from django.contrib import admin


app_name='blog'

urlpatterns = [
    path('', news_redirect),
    path('news/', PostsList.as_view(), name='posts_list'),
   # path('account/login/', LoginView.as_view(), name='login'),
    path('news/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('search/', SearchPosts.as_view(), name='search_posts'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    # path('add/', new_add)
    # path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    # path('categories/<int:pk>'/subscribe, subscribe, name='subscribe')
]