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

    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    images = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Posts
        fields = [
            'id',
            'name',
            'description',
            'category_id',
            'category',
            'images',
            'uploaded_images',
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
        upload_images = validated_data.pop("uploaded_images")

        with transaction.atomic():
            post = Posts.objects.create(**validated_data)

            for img in upload_images:
                PostImage.objects.create(
                    post=post,
                    user=User.objects.filter(pk=1).first(),
                    image=img
                )

        return post

    def validate_category_id(self, value):
        if value == 0:
            raise serializers.ValidationError({"category_id": "Category id cannot be 0"})
        return value
