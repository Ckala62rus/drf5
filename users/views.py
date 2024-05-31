import logging

from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from rest_framework.generics import RetrieveAPIView

from drf_spectacular.utils import extend_schema_view, extend_schema

from users.serializers.api.user_serializer import UserSerializer
from users.models.users import User
from users.serializers.api.user_serializer import UserMeSerializer
from users.serializers.api.user_serializer import ChangePasswordSerializer
from users.user_service import email_notification


# Create your views here.

@extend_schema_view(
    post=extend_schema(
        request=ChangePasswordSerializer,
        responses=None,
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
    get=extend_schema(
        description="Get current user model",
        summary="Get current user model",
        tags=["Пользователи"],
    ),
)
class Me(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserMeSerializer

    # Так как RetrieveAPIView ищет обьект по id, мы меняем это поведение
    # Передав модель залогиненного пользователя
    def get_object(self):
        log = logging.getLogger(__name__)
        log.info("new logger")
        return self.request.user

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return UserMeSerializer

    def get(self, request, *args, **kwargs):
        email_notification.delay(
            "some text for test queue celery",
            "admin@mail.ru"
        )
        return self.retrieve(request, *args, **kwargs)

    # def get(self, request: WSGIRequest) -> JsonResponse:
    #     user = request.user
    #     serializer = UserMeSerializer(data=user.__dict__)
    #     serializer.is_valid(raise_exception=True)
    #     return JsonResponse(serializer.data, status=status.HTTP_200_OK)
