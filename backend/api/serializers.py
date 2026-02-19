from rest_framework import serializers
from .models import Post, Resource, TeamMember, ContactMessage


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'content',
            'image', 'created_at', 'updated_at',
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = [
            'id', 'title', 'description', 'file',
            'category', 'created_at',
        ]
        read_only_fields = ['created_at']


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = [
            'id', 'name', 'title', 'bio',
            'photo', 'university', 'order',
        ]


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = [
            'id', 'name', 'email', 'subject',
            'message', 'created_at', 'is_read',
        ]
        read_only_fields = ['created_at', 'is_read']
