from rest_framework import serializers
from flace.models import User, Post


class PostSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post
		fields = ('id', 'title', 'slug', 'description', 'content', 'published', 'created', 'author', 'last_edited')

class UserSerializer(serializers.Serializer):

	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'display_name')