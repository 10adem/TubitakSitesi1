from rest_framework import viewsets, permissions
from .models import Post, Resource, TeamMember, ContactMessage
from .serializers import (
    PostSerializer, ResourceSerializer,
    TeamMemberSerializer, ContactMessageSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    """
    Public: list & retrieve posts.
    Admin: create, update, delete.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class ResourceViewSet(viewsets.ModelViewSet):
    """
    Public: list & retrieve resources.
    Admin: create, update, delete.
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class TeamMemberViewSet(viewsets.ModelViewSet):
    """
    Public: list & retrieve team members.
    Admin: create, update, delete.
    """
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class ContactMessageViewSet(viewsets.ModelViewSet):
    """
    Public: create (send) contact messages.
    Admin: list, retrieve, update, delete.
    """
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def get_permissions(self):
        if self.action == 'create':
            # Anyone can send a contact message
            return [permissions.AllowAny()]
        # Only admins can read / modify messages
        return [permissions.IsAdminUser()]
