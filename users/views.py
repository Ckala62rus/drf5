from django.core.handlers.wsgi import WSGIRequest
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework import viewsets, permissions, status
from rest_framework.generics import CreateAPIView

from drf_spectacular.utils import extend_schema_view, extend_schema
from django.http import JsonResponse

from api.serializers import UserSerializer
from users.models.users import User
from users.serializers.api.user_serializer import UserMeSerializer
from users.serializers.api.user_serializer import ChangePasswordSerializer


# Create your views here.

@extend_schema_view(
    post=extend_schema(
        request=ChangePasswordSerializer,
        summary='Смена пароля', tags=['Пользователи']),
)
class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(
            instance=user, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_204_NO_CONTENT)
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MzYxMzE5LCJpYXQiOjE3MTYyNzQ5MTksImp0aSI6IjA3ZjE5ZDhjODgyNTQ4MmRhNzIzYjM3Y2ExY2VlY2YyIiwidXNlcl9pZCI6MX0.4Els0XpvYfHbOoB9HXHkSgDlIs_4lP9OEUr8IvHIL1c
# pbkdf2_sha256$720000$Dm740NKSKCvuXXPefn9IwK$OIBCH10l5qjBkuGyJdfP+nLVQtayVHFQaa54OytdEV0=


# Create your models here.
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


@extend_schema_view(
    post=extend_schema(
        description="Get current user model",
        summary="Get current user model",
        tags=["Пользователи"],
    ),
)
class Me(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: WSGIRequest) -> JsonResponse:
        user = request.user
        serializer = UserMeSerializer(data=user.__dict__)
        serializer.is_valid(raise_exception=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MzEzOTM2LCJpYXQiOjE3MTYyMjc1MzYsImp0aSI6IjdjMTc1ODIzMGYwMTRmOGNhZjRkZTgyNjViOGQ2Nzc3IiwidXNlcl9pZCI6MX0.JujZghyItKXQlGm_c2l5jKoOdxOCX7y1gTLSdyE66pg
