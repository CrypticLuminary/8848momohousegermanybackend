from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import FranchiseFAQ, FranchiseInquiry
from .serializers import FranchiseFAQSerializer, FranchiseInquiryAdminSerializer, FranchiseInquiryCreateSerializer


class PublicFranchiseFAQViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FranchiseFAQSerializer

    def get_queryset(self):
        return FranchiseFAQ.objects.filter(is_active=True)


class PublicFranchiseInquiryViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = FranchiseInquiry.objects.all()
    serializer_class = FranchiseInquiryCreateSerializer


class AdminFranchiseFAQViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = FranchiseFAQ.objects.all()
    serializer_class = FranchiseFAQSerializer


class AdminFranchiseInquiryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = FranchiseInquiry.objects.all()
    serializer_class = FranchiseInquiryAdminSerializer
