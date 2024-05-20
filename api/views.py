from django.contrib.auth.models import Group
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema, extend_schema_view

from rest_framework import viewsets, permissions, serializers, status, generics, mixins
from rest_framework.decorators import permission_classes, api_view, action
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CategorySerializer, GroupSerializer, UserSerializer, PostSerializer
from blog.models import Categories, Posts
from users.models.users import User


# Create your views here.

@extend_schema(tags=["Posts"])
@extend_schema_view(
    list=extend_schema(
        description="Retrieve all post with pagination",
        summary='Get all posts'
    ),
    create=extend_schema(
        description="Create new post",
        # parameters=[
        #     OpenApiParameter('title', description='Title of the post', required=True),
        #     OpenApiParameter('description', description='Title of the post', required=False),
        #     OpenApiParameter('category_id', description='Category id', required=True)
        # ],
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
        # queryset = self.filter_queryset(self.get_queryset())
        #
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response({'data': serializer.data, "test": 'hello world'})
        #
        # serializer = self.get_serializer(queryset, many=True)
        # return Response(serializer.data,)

    # def update(self, request, *args, **kwargs):
        # pass


@extend_schema(
    description='Override a specific method',
    tags=["Categories"]
)
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Categories.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    @action(methods=['GET'], detail=False)
    def clear(self, request: WSGIRequest) -> JsonResponse:
        return JsonResponse({'testing': 'my custom function'})


@extend_schema_view(
    post=extend_schema(
        description='aaaaa',
        summary="wwwww",
        tags=["A"],
    ),
)
class Some(CreateAPIView):
    def post(self, request: WSGIRequest) -> JsonResponse:
        return JsonResponse({'testing': 'some class + clear metgod'})


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
    # permission_classes = [permissions.IsAuthenticated]


@extend_schema_view(
    list=extend_schema(
        description='Получение всех пользователей',
        summary="Получение всех пользователей",
        tags=["Пользователи"],
    ),
    create=extend_schema(
        description='Создание пользователя',
        summary="Создание пользователя",
        tags=["Пользователи"],
    ),
    retrieve=extend_schema(
        description="Получение пользователя по идентификатору 'id'",
        summary="Получение пользователя по идентификатору 'id'",
        tags=["Пользователи"],
    ),
    update=extend_schema(
        description="Обновление пользователя по идентификатору 'id'",
        summary="Обновление пользователя по идентификатору 'id'",
        tags=["Пользователи"],
    ),
    partial_update=extend_schema(
        description="Частичное обновление пользователя по идентификатору 'id'",
        summary="Частичное обновление пользователя по идентификатору 'id'",
        tags=["Пользователи"],
    ),
    destroy=extend_schema(
        description="Удаление пользователя по идентификатору 'id'",
        summary="Удаление обновление пользователя по идентификатору 'id'",
        tags=["Пользователи"],
    ),
)
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# https://drf-spectacular.readthedocs.io/en/latest/
# class SnippetSerializer(generics.GenericAPIView):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     def get(self, request, pk, format=None) -> Response:
#         """Get method for categories.
#
#         Args:
#             request (_type_): _description_
#             pk (_type_): _description_
#             format (_type_, optional): _description_. Defaults to None.
#
#         Returns:
#             Response: _description_
#         """
#         users = Categories.objects.all()
#         serializer_class = CategorySerializer(users, many=True)
#         # data = request.query_params
#         # return JsonResponse(dict(data), status=status.HTTP_200_OK)
#         ress = serializer_class.data
#         return Response(serializer_class.data, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         dataIn = request.data['name']
#         return JsonResponse({'a': 'hello world'})
#
    # @action(methods=['GET'], detail=False)
    # def clear(request: WSGIRequest) -> JsonResponse:
    #     return JsonResponse({'testing': 'my custom function'})