from django.shortcuts import render
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView

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
