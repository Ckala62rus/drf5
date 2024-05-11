from django.contrib.auth.models import Group, User
from django.http import JsonResponse

from rest_framework import viewsets, permissions, serializers, status
from rest_framework.decorators import permission_classes, api_view
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
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get(self, request, pk, format=None) -> Response:
        """Get method for categories.

        Args:
            request (_type_): _description_
            pk (_type_): _description_
            format (_type_, optional): _description_. Defaults to None.

        Returns:
            Response: _description_
        """
        users = Categories.objects.all()
        serializer_class = CategorySerializer(users, many=True)
        # data = request.query_params
        # return JsonResponse(dict(data), status=status.HTTP_200_OK)
        ress = serializer_class.data
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        dataIn = request.data['name']
        return JsonResponse({'a': 'hello world'})

    @api_view(['GET'])
    def clear(request):
        return JsonResponse({'testing': 'my custom function'})
