from django.contrib.auth.models import Group
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse

from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework import viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import CategorySerializer, GroupSerializer, UserSerializer, PostSerializer
from blog.models import Categories, Posts
from users.models.users import User
from users.serializers.api.user_serializer import UserMeSerializer


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
