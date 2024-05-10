from django.contrib.auth.models import Group, User
from rest_framework import viewsets, permissions, serializers
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CategorySerializer, GroupSerializer, UserSerializer
from blog.models import Categories


# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Categories.objects.all()
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class SnippetSerializer(APIView):

    def get(self, request, format=None):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Response({'a':'hello world'})

    def post(self, request, format=None):
        dataIn = request.data['name']
        return Response({'a': 'hello world'})