from rest_framework import routers
from .views import ArticleViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls))
]