from rest_framework.routers import DefaultRouter

from .views import PublicFranchiseFAQViewSet, PublicFranchiseInquiryViewSet

router = DefaultRouter()
router.register("faq", PublicFranchiseFAQViewSet, basename="franchise-faq")
router.register("inquiries", PublicFranchiseInquiryViewSet, basename="franchise-inquiries")

urlpatterns = router.urls
