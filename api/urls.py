from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register("categories", views.CategoryViewSet)
router.register("groups", views.GroupViewSet)
router.register("users", views.UserViewSet)

# router.register(r"test", views.SnippetSerializer, basename='MyModel')

urlpatterns = [
    path('test/', views.SnippetSerializer.as_view(), name="instances"),
]

urlpatterns.extend(router.urls)
