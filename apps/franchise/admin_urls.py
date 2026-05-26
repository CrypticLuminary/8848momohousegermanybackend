from rest_framework.routers import DefaultRouter

from .views import AdminFranchiseFAQViewSet, AdminFranchiseInquiryViewSet

router = DefaultRouter()
router.register("faq", AdminFranchiseFAQViewSet, basename="admin-franchise-faq")
router.register("inquiries", AdminFranchiseInquiryViewSet, basename="admin-franchise-inquiries")

urlpatterns = router.urls
