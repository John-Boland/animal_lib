from django.urls import path

from animal_liberation.articles.views import (ArticleListView, DraftListView,
                                             CreateArticleView, EditArticleView,
                                             DetailArticleView)

app_name = 'articles'

urlpatterns = [
    path("", ArticleListView.as_view(), name="list"),
    path("write-new-article/", CreateArticleView.as_view(), name="write_new"),
    path("drafts/", DraftsListView.as_view(), name="drafts"),
    path("edit/<pk:pk>/", EditArticleView.as_view(), name="edit_article"),
    path("<slug:slug>/", DetailArticleView.as_view(), name="article"),
]
