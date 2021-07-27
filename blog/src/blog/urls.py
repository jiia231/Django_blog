from django.urls import path

from .views import ArticlesListView, DetailArticleView, FeedbackView

urlpatterns = [
    path('', ArticlesListView.as_view(), name='articles_list'),
    path('feedback', FeedbackView.as_view(), name='feedback'),
    path('<str:article_id>', DetailArticleView.as_view(), name='article_detail'),
]
