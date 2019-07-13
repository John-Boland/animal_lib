from django.urls import path
from animal_lib.news.views import NewsListView, NewsDeleteView
from animal_lib.news import views

app_name = 'news'

urlpatterns = [
    path("", NewsListView.as_view(), name="list"),
    path("delete/<int:pk>/", NewsDeleteView.as_view(template_name="news/news_confirm_delete.html"), name="delete_news"),
    path("post-news/", views.post_news, name='post_news'),
    path("like/", views.like, name="like_post"),
    path("get-thread/", views.get_thread, name='get_thread'),
    path("post-comment/", views.post_comment, name='post_comments'),
    path("update-interactions/", views.update_interactions, name="update_interactions"),
]
