from django.urls import include, path
from .views import BlogViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BlogViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
]
