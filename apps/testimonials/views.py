from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Testimonial
from .serializers import TestimonialSerializer


class PublicTestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TestimonialSerializer

    def get_queryset(self):
        return Testimonial.objects.filter(is_active=True)


class AdminTestimonialViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
