import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(_('Название'), max_length=255)
    content = RichTextUploadingField(_('Содержимое'), blank=True)
    created_at = models.DateTimeField(_('Создано в'), default=now)
    tags = models.ManyToManyField("Tag", related_name='articles', through="ArticleTags")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog"."article'
        verbose_name = _('Статья')
        verbose_name_plural = _('Статьи')


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_('Название'), max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog"."tag'
        verbose_name = _('Тег')
        verbose_name_plural = _('Теги')


class ArticleTags(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog"."articletags'
        unique_together = ('article', 'tag')


class Feedback(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(_('Имя'), max_length=120)
    email = models.EmailField(_('Email'), )
    message = models.TextField(_('Сообщение'), )

    def __str__(self):
        return 'Сообщение от ' + str(self.name)

    class Meta:
        db_table = 'blog"."feedback'
        verbose_name = _('Сообщение')
        verbose_name_plural = _('Сообщения')
