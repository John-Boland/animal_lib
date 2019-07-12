from django.urls import path

from .views import (ArticleListView, DraftListView, CreateArticleView, EditArticleView, DetailArticleView)

app_name = 'articles'

urlpatterns = [
    path("", ArticleListView.as_view(), name="list"),
    path("write-new-article/", CreateArticleView.as_view(), name="write_new"),
    path("drafts/", DraftListView.as_view(), name="drafts"),
    path("edit/<int:pk>/", EditArticleView.as_view(), name="edit_article"),
    path("<slug:title>/", DetailArticleView.as_view(), name="article"),
]
