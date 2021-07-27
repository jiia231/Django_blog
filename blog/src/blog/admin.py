from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from .models import Article, Tag, ArticleTags, Feedback


class ArticleContentAdminForm(forms.ModelForm):
    content = forms.CharField(label='Содержимое', widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleTagsInline(admin.TabularInline):
    model = ArticleTags
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at',)
    readonly_fields = ('created_at',)

    list_filter = ('author',)
    form = ArticleContentAdminForm
    search_fields = ('title', 'content',)

    fields = (
        'author', 'title', 'content', 'created_at',
    )

    inlines = [
        ArticleTagsInline,
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

    search_fields = ('name',)

    fields = (
        'id', 'name',
    )
    readonly_fields = ('id',)

    inlines = [
        ArticleTagsInline,
    ]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)

    readonly_fields = ('id', 'name', 'email', 'message')
