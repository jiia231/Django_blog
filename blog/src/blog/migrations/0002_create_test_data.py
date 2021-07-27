from django.contrib.auth.models import User
from django.db import migrations

from ..models import Tag, Article


def create_data(*args):
    admin = User.objects.create_superuser(username='admin', email='admin@example.com', password='password')
    admin.save()

    tag1 = Tag(name='Journeys')
    tag2 = Tag(name='Food')
    tag3 = Tag(name='Sports')
    tag4 = Tag(name='Good day')
    tag5 = Tag(name='Awesome day')
    Tag.objects.bulk_create([tag1, tag2, tag3, tag4, tag5])

    article1 = Article(author=admin, title='My First Article')
    article2 = Article(author=admin, title='New Recipe')
    article3 = Article(author=admin, title='Snowboarding with my friends')
    article4 = Article(author=admin, title='My Collection of Rarest Vinyls')
    article5 = Article(author=admin, title='Going Camping!')
    article6 = Article(author=admin, title='My Promotion')
    Article.objects.bulk_create([article1, article2, article3, article4, article5, article6])

    tag1.articles.set([article3, article5])
    tag2.articles.set([article2])
    tag3.articles.set([article3])
    tag4.articles.set([article2, article4])
    tag5.articles.set([article1, article6])


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
