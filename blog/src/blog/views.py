from django.shortcuts import redirect
from django.shortcuts import render
from rest_framework import views
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .forms import FeedBackForm
from .models import Article
from .serializers import ListArticleSerializer, DetailArticleSerializer


class ArticlesListView(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'articles_list.html'

    def get(self, request):
        queryset = Article.objects.all().prefetch_related('tags')
        date_sort = request.query_params.get('date_sort', 'desc')
        if date_sort == 'desc':
            queryset = queryset.order_by('-created_at', )
        elif date_sort == 'asc':
            queryset = queryset.order_by('created_at', )
        tag = request.query_params.get('tag')
        if tag:
            queryset = queryset.filter(articletags__tag__name=tag)
        serializer_for_queryset = ListArticleSerializer(
            instance=queryset,
            many=True,
        )

        return Response({"articles": serializer_for_queryset.data})


class DetailArticleView(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'article_detail.html'

    def get(self, request, article_id):
        queryset = Article.objects.prefetch_related('tags').get(id=article_id)
        serializer_for_queryset = DetailArticleSerializer(
            instance=queryset,
        )

        return Response({"article": serializer_for_queryset.data})


class FeedbackView(views.View):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'feedback_form.html'

    def get(self, request):
        form = FeedBackForm()

        return render(request, 'feedback_form.html', {'form': form})

    def post(self, request, **kwargs):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('articles_list')
