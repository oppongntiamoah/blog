from .serializers import PostSerializer, UserSerializer
from rest_framework import viewsets


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.published.all()
    serializer_class = PostSerializer


class UserViewser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer