from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MappingViewSet

router = DefaultRouter()
router.register('', MappingViewSet, basename='mappings')

urlpatterns = [
    path('', include(router.urls)),
]