from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import BlogPost
from .serializers import BlogPostSerializer


class PublicBlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = "slug"
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.filter(status=BlogPost.Status.PUBLISHED)


class AdminBlogPostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
