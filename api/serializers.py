from django.contrib.auth.models import Group
from rest_framework import serializers

from blog.models import Categories, Posts
from users.models.users import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'description']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField('get_created_at')
    updated_at = serializers.SerializerMethodField('get_updated_at')
    category = CategorySerializer(many=False, read_only=True)

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

    def get_created_at(self, post):
        return post.created_at.strftime('%Y-%m-%d %H:%M:%S')

    def get_updated_at(self, post):
        return post.updated_at.strftime('%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        name = validated_data.get('name')
        description = validated_data.get('description')
        category_id = validated_data.get('category_id').id
        return Posts.objects.create(
            name=name,
            description=description,
            category_id=category_id
        )

