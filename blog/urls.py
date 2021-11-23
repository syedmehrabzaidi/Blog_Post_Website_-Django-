from django.urls import path

from profiles.views import ProfilesDetailView
from .views import (BlogListView, BlogDetailView,
                    BlogCreateView, BlogUpdateView,
                    BlogDeleteView, follower_list, following_list,
                    CommentCreateView, LikeView, LikeViewHome,)

urlpatterns = [
    path(
        '',
        BlogListView.as_view(),
        name='home'
    ),
    path(
        'post/<int:pk>/',
        BlogDetailView.as_view(),
        name='post_detail'
    ),
    path(
        'post/new/', BlogCreateView.as_view(),
        name='post_new'
    ),
    path(
        'comment/<int:pk>/', CommentCreateView.as_view(),
        name='post_comment'
    ),
    path(
        'blogpost-like/<int:pk>', LikeView.as_view(),
        name="blogpost_like"
    ),path(
        'post-like/<int:pk>', LikeViewHome.as_view(),
        name="post_like"
    ),
    path(
        'post/<int:pk>/edit/',
        BlogUpdateView.as_view(),
        name='post_edit'
    ),
    path(
        'post/<int:pk>/delete/',
        BlogDeleteView.as_view(),
        name='post_delete'
    ),
    path(
        'post/<int:pk>/',
        ProfilesDetailView.as_view(),
        name='profile-detail-view'
    ),
    path(
        'follower_list/',
        follower_list,
        name='follower-list'
    ),
    path(
        'following_list/',
        following_list,
        name='following-list'
    ),

]
