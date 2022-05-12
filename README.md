# Django Blog

### Description

A personal Django blog with a tagging system and an article editor with html markup support.

### Launch

Use docker-compose to run.

```bash
docker-compose -f docker-compose.yaml up --build
```

It will run a blog, database, and nginx in docker containers. The blog will be launched via gunicorn.


### Usage

1. Go to the admin panel at **localhost/admin**. On startup, a superuser is automatically created with username **admin** and password **password**.
2. Here you can create tags, write articles. The article editor supports adding images, changing text style, creating lists, and more.
3. Create or edit an article, add an image to it.
4. Check how it is displayed at **localhost/articles**
5. Here you can view all articles, sort them by publication date, filter by tags
6. By clicking on the article title, you can go to its page, where full article will be displayed
