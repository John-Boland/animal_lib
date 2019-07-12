from django.urls import path

from animal_lib.articles.views import ArticleListView, DraftListView, CreateArticleView, EditArticleView, DetailArticleView
from animal_lib.articles.forms import ArticleForm
app_name = 'articles'

urlpatterns = [
    path("", ArticleListView.as_view(), name="list"),
    path("write-new-article/", CreateArticleView.as_view(form_class=ArticleForm, template_name="articles/article_create.html"), name="write_new"),
    path("articles/drafts/", DraftListView.as_view(), name="drafts"),
    path("articles/edit/<int:pk>/", EditArticleView.as_view(), name="edit_article"),
    path("articles/<slug:title>/", DetailArticleView.as_view(), name="article"),
]
