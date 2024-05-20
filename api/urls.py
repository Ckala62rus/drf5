from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework.routers import DefaultRouter

from blog.views import (
    CategoryViewSet,
    GroupViewSet,
    PostViewSet,
    UserViewSet,
    Me,
)

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("groups", GroupViewSet)
router.register("users", UserViewSet)


urlpatterns = [
    # Spectacular documentation Swagger/OpenApi
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),

    # Djoser JWT auth
    path('auth/', include('djoser.urls.jwt')),

    # path('test/', views.SnippetNewSerializer.clear, name="instances"),
    path('test/', CategoryViewSet.clear, name="instances"),
    path('me/', Me.as_view(), name="Пользователи"),

    path('posts/', PostViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name="Posts"),
]

urlpatterns.extend(router.urls)
