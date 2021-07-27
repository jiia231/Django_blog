from rest_framework import serializers

from .models import Article, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class ListArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'created_at', 'tags',)


class DetailArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'content', 'created_at', 'tags',)
