from rest_framework import serializers

from users.models.users import User


class UserMeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', max_length=255)
    email = serializers.EmailField(source='user.email')
    id = serializers.IntegerField(source='user.id')

    class Meta:
        model = User
        fields = ["id", "username", "email"]
