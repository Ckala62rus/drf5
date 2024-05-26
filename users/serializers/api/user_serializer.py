from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from blog.models import Posts, Categories
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'description']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField('get_created_at')
    updated_at = serializers.SerializerMethodField('get_updated_at')
    category = CategorySerializer(many=False, read_only=True)
    category_id = serializers.IntegerField(required=True, write_only=True)

    class Meta:
        model = Posts
        fields = [
            'id',
            'name',
            'description',
            'category_id',
            'category',
            'created_at',
            'updated_at'
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_created_at(self, post):
        return post.created_at.strftime('%Y-%m-%d %H:%M:%S')

    @extend_schema_field(OpenApiTypes.STR)
    def get_updated_at(self, post):
        return post.updated_at.strftime('%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        name = validated_data.get('name')
        description = validated_data.get('description')
        category_id = validated_data.get('category_id')
        return Posts.objects.create(
            name=name,
            description=description,
            category_id=category_id
        )

    def validate_category_id(self, value):
        if value == 0:
            raise serializers.ValidationError({"category_id": "Category id cannot be 0"})
        return value
