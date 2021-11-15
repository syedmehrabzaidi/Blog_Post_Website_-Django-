from .views import PostListCreateApiView, PostDetailApiView

from django.urls import path

urlpatterns = [
    path('post/<int:pk>/', PostDetailApiView.as_view()),
    path('post/', PostListCreateApiView.as_view()),
]
