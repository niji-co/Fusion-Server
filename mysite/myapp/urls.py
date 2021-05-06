from django.conf.urls import include, url
from myapp.views import hello, viewArticle, viewArticles

urlpatterns = [
    url(r'^hello/', hello, name = 'hello'),
    url(r'^article/(\d+)/', viewArticle, name = 'article'),
    url(r'^articles/(\d{2})/(\d{4})', viewArticles, name = 'articles'),
]
