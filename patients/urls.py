from django.urls import path,include
from .views import PatientViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PatientViewSet, basename='patients')

urlpatterns = [
    path('', include(router.urls)),
]