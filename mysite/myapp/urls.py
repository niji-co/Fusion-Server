from django.conf.urls import include, url
from myapp.views import hello, viewArticle, viewArticles

from rest_framework import routers
from .import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

urlpatterns = [
    url(r'^hello/', hello, name = 'hello'),
    url(r'^article/(\d+)/', viewArticle, name = 'article'),
    url(r'^articles/(\d{2})/(\d{4})', viewArticles, name = 'articles'),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
    namespace='rest_framework'))
]
