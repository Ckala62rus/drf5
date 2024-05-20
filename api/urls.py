from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register("categories", views.CategoryViewSet)
router.register("groups", views.GroupViewSet)
router.register("users", views.UserViewSet)


urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),

    # Djoser JWT auth
    path('auth/', include('djoser.urls.jwt')),

    # path('test/', views.SnippetNewSerializer.clear, name="instances"),
    path('test/', views.CategoryViewSet.clear, name="instances"),

    path('some/', views.Some.as_view(), name="A"),

    path('posts/', views.PostViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name="Posts"),
]

urlpatterns.extend(router.urls)
