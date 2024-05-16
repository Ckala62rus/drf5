from django.urls import path
from drf_spectacular import openapi
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from api import views

router = DefaultRouter()
router.register("categories", views.CategoryViewSet)
router.register("groups", views.GroupViewSet)
router.register("users", views.UserViewSet)
# router.register("posts", views.PostViewSet)

# router.urls.append('test/', views.SnippetSerializer.as_view())

urlpatterns = [
    # path('test/', views.SnippetSerializer.as_view(), name="instances"),
    # path('test/<int:pk>', views.SnippetSerializer.as_view(), name="instances"),


    # path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='api-docs'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),

    # path('test/', views.SnippetNewSerializer.clear, name="instances"),
    path('test/', views.CategoryViewSet.clear, name="instances"),

    path('posts/', views.PostViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name="Posts"),
]

urlpatterns.extend(router.urls)
