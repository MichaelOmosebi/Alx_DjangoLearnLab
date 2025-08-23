from django.urls import path
from django.contrib.auth import views as auth_views
from .views import BlogsView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'blog'   # 👈 this gives it the 'blog:' namespace

urlpatterns = [
    path('blogs/', BlogsView.as_view(), name='home'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
