from django.urls import path

from users.views import ChangePasswordView, Me

urlpatterns = [
    path('change-password/', ChangePasswordView.as_view(), name="Change password"),
    path('me/', Me.as_view(), name="Пользователи"),
]
