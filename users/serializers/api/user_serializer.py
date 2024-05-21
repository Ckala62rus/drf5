from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from users.models.users import User


class UserMeSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', max_length=255)
    # email = serializers.EmailField(source='user.email')
    # id = serializers.IntegerField(source='user.id')

    class Meta:
        model = User
        fields = ["id", "username", "email"]
        # fields = "__all__"


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True, max_length=20)
    new_password = serializers.CharField(required=True, max_length=20, write_only=True)

    class Meta:
        model = User
        fields = ["old_password", "new_password"]

    def validate(self, attrs):
        user = self.instance
        old_password = attrs.pop('old_password')
        if not user.check_password(old_password):
            raise ParseError(
                'Проверьте правильность текущего пароля.'
            )
        return attrs

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def update(self, instance, validated_data):
        password = validated_data.pop('new_password')
        instance.set_password(password)
        instance.save()
        return instance
