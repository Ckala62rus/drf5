from django.contrib.auth.models import Group
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse

from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import CategorySerializer, GroupSerializer, PostSerializer
from blog.models import Categories, Posts


# Create your views here.

@extend_schema(tags=["Posts"])
@extend_schema_view(
    list=extend_schema(
        description="Retrieve all post with pagination",
        summary='Get all posts'
    ),
    create=extend_schema(
        description="Create new post",
    ),
)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

    @extend_schema(
        summary="Create post",
        description="Create new post and return model"
    )
    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


@extend_schema_view(
    create=extend_schema(description='Создание категории', summary='Создание категории', tags=['Категории']),
    list=extend_schema(description='Получение всех категорий', summary='Получение всех категорий', tags=['Категории']),
    retrieve=extend_schema(description='Получение категории по id', summary='Получение категории по id', tags=['Категории']),
    update=extend_schema(description='Обновление категории по id', summary='Обновление категории по id', tags=['Категории']),
    partial_update=extend_schema(description='Частичное обновление категории по id', summary='Частичное обновление категории по id', tags=['Категории']),
    destroy=extend_schema(description='Удаление категории по id', summary='Удаление категории по id', tags=['Категории']),
    clear=extend_schema(description='Common method in class', summary='Common method in class', tags=['Категории']),
)
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Categories.objects.all()

    @action(methods=['GET'], detail=False)
    def clear(self, request: WSGIRequest) -> JsonResponse:
        return JsonResponse({'testing': 'my custom function'})


@extend_schema(
    description='Override a specific method',
    tags=["Group"]
)
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
