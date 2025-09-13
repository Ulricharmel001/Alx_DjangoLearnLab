from rest_framework import serializers
from .models import Post, Comment
from django.conf import settings

User = settings.AUTH_USER_MODEL

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_username', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'author_username', 'title', 'content', 'created_at', 'updated_at', 'comments']
        read_only_fields = ['author', 'created_at', 'updated_at', 'comments']

    def create(self, validated_data):
        # automatically set the author to the logged-in user
        request = self.context.get('request')
        user = request.user if request else None
        return Post.objects.create(author=user, **validated_data)
