from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from blog.models import Post

from .serializers import PostSerializer


class PostListCreateApiView(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]




class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]


