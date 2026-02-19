from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'resources', views.ResourceViewSet, basename='resource')
router.register(r'team', views.TeamMemberViewSet, basename='teammember')
router.register(r'contact', views.ContactMessageViewSet, basename='contactmessage')

urlpatterns = [
    path('', include(router.urls)),
]
