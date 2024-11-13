from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()


router.register(r'user', UserViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'article', ArticleViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
