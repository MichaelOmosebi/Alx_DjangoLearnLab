from django.shortcuts import render

###########################################
# --------- USING VIEWSETS -------------
###########################################

from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    """
    Handles all CRUD operations for posts:
    - list: GET /posts/
    - retrieve: GET /posts/{id}/
    - create: POST /posts/
    - update: PUT /posts/{id}/
    - partial_update: PATCH /posts/{id}/
    - destroy: DELETE /posts/{id}/
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'content']
    filterset_fields = ['author__username']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Handles all CRUD operations for comments:
    - list: GET /posts/{post_pk}/comments/
    - retrieve: GET /posts/{post_pk}/comments/{id}/
    - create: POST /posts/{post_pk}/comments/
    - update: PUT /posts/{post_pk}/comments/{id}/
    - partial_update: PATCH /posts/{post_pk}/comments/{id}/
    - destroy: DELETE /posts/{post_pk}/comments/{id}/
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_pk')
        return Comment.objects.filter(post_id=post_id).order_by('-created_at')

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_pk')
        serializer.save(author=self.request.user, post_id=post_id)


###################################################
# --------- USING CBF GenericAPI View -------------
###################################################

# # Create your views here.
# from rest_framework import generics, permissions, filters
# from rest_framework.pagination import PageNumberPagination
# from django.shortcuts import get_object_or_404

# from .models import Post, Comment
# from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer
# from .permissions import IsOwnerOrReadOnly


# class DefaultPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 100


# # POSTS

# class PostListCreateView(generics.ListCreateAPIView):
#     queryset = Post.objects.select_related('author').all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     pagination_class = DefaultPagination

#     # simple filtering (search + ordering)
#     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
#     search_fields = ['title', 'content']              # ?search=foo
#     ordering_fields = ['created_at', 'updated_at']    # ?ordering=-created_at

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)


# class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.select_related('author').prefetch_related('comments')
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     pagination_class = None

#     def get_serializer_class(self):
#         # On detail, include nested comments for convenience
#         if self.request.method in ('GET',):
#             return PostDetailSerializer
#         return PostSerializer


# # NESTED COMMENTS: /posts/<post_id>/comments/

# class PostCommentListCreateView(generics.ListCreateAPIView):
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     pagination_class = DefaultPagination

#     def get_queryset(self):
#         post_id = self.kwargs['post_id']
#         return Comment.objects.filter(post_id=post_id).select_related('author', 'post')

#     def perform_create(self, serializer):
#         post_id = self.kwargs['post_id']
#         post = get_object_or_404(Post, pk=post_id)
#         serializer.save(author=self.request.user, post=post)


# # Comment detail (edit/delete own comment)
# class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.select_related('author', 'post')
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     # pagination_class = None