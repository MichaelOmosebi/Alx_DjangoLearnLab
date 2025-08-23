from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (BlogsView, PostListView, PostDetailView, PostCreateView,
                    PostUpdateView, PostDeleteView, CommentUpdateView,
                    CommentDeleteView, CommentCreateView, search_posts, PostByTagListView)

app_name = 'blog'   # 👈 this gives it the 'blog:' namespace

urlpatterns = [
    path('blogs/', BlogsView.as_view(), name='home'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('search/', search_posts, name='search_posts'),
     path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='tagged-posts'),
]
