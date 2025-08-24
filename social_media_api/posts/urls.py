from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # posts
    path('', views.PostListCreateView.as_view(), name='post-list-create'),
    path('<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),

    # nested comments under a post
    path('<int:post_id>/comments/', views.PostCommentListCreateView.as_view(), name='post-comments'),

    # single comment (edit/delete)
    path('comments/<int:pk>/', views.CommentRetrieveUpdateDestroyView.as_view(), name='comment-detail'),
]
# Note: No trailing slashes in URLs as per requirement