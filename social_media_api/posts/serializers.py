from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']


# class CommentSerializer(serializers.ModelSerializer):
#     author_username = serializers.ReadOnlyField(source='author.username')

#     class Meta:
#         model = Comment
#         fields = ['id', 'post', 'author', 'author_username', 'content', 'created_at', 'updated_at']
#         read_only_fields = ['id', 'author', 'post', 'created_at', 'updated_at']


# class PostSerializer(serializers.ModelSerializer):
#     author_username = serializers.ReadOnlyField(source='author.username')
#     comments_count = serializers.IntegerField(source='comments.count', read_only=True)

#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'content', 'author', 'author_username',
#                   'comments_count', 'created_at', 'updated_at']
#         read_only_fields = ['id', 'author', 'comments_count', 'created_at', 'updated_at']


# # Optional: lightweight nested comments list for post detail
# class PostDetailSerializer(PostSerializer):
#     comments = CommentSerializer(many=True, read_only=True)

#     class Meta(PostSerializer.Meta):
#         fields = PostSerializer.Meta.fields + ['comments']
#         read_only_fields = PostSerializer.Meta.read_only_fields + ['comments']