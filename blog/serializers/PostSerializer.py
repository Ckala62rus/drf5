from django.db import transaction
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from blog.models import Posts, PostImage
from blog.serializers.PostImageSerializer import PostImageSerializer
from users.models.users import User
from users.serializers.api.user_serializer import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField('get_created_at')
    updated_at = serializers.SerializerMethodField('get_updated_at')
    category = CategorySerializer(many=False, read_only=True)
    category_id = serializers.IntegerField(required=True, write_only=True)
    image = serializers.ImageField(required=False)
    images = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Posts
        fields = [
            'id',
            'name',
            'description',
            'category_id',
            'category',
            'image',
            'images',
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
        upload_images = validated_data.pop("image")

        with transaction.atomic():
            name = validated_data.get('name')
            description = validated_data.get('description')
            category_id = validated_data.get('category_id')
            post = Posts.objects.create(
                name=name,
                description=description,
                category_id=category_id
            )

            PostImage.objects.create(
                # name=name,
                post=post,
                user=User.objects.filter(pk=1).first(),
                image=upload_images
            )

        return post

    def validate_category_id(self, value):
        if value == 0:
            raise serializers.ValidationError({"category_id": "Category id cannot be 0"})
        return value
