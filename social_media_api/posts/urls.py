from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedViewSet, LikePostView, UnlikePostView

# Main router for posts
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

# Nested router for comments under posts
posts_router = NestedDefaultRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

feeds_router = DefaultRouter()
feeds_router.register(r'feed', FeedViewSet, basename='user-feed')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
    #path('', include(feeds_router.urls)),

    # Explicit feed route --- for checker
    path('feed/', FeedViewSet.as_view({'get': 'list'}), name='user-feed'),

    # Explicit like/unlike endpoints
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='post-like'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='post-unlike'),
]


# app_name = 'posts'

# urlpatterns = [
#     # posts
#     path('', views.PostListCreateView.as_view(), name='post-list-create'),
#     path('<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),

#     # nested comments under a post
#     path('<int:post_id>/comments/', views.PostCommentListCreateView.as_view(), name='post-comments'),

#     # single comment (edit/delete)
#     path('comments/<int:pk>/', views.CommentRetrieveUpdateDestroyView.as_view(), name='comment-detail'),
# ]
# # Note: No trailing slashes in URLs as per requirement