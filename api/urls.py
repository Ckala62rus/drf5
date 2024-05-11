from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register("categories", views.CategoryViewSet)
router.register("groups", views.GroupViewSet)
router.register("users", views.UserViewSet)

# router.urls.append('test/', views.SnippetSerializer.as_view())

urlpatterns = [
    path('test/', views.SnippetSerializer.as_view(), name="instances"),
    path('test/<int:pk>/', views.SnippetSerializer.as_view(), name="instances"),
    path('test-test', views.SnippetSerializer.clear, name="instances"),
]

urlpatterns.extend(router.urls)
