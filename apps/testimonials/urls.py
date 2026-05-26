from rest_framework.routers import DefaultRouter

from .views import PublicTestimonialViewSet

router = DefaultRouter()
router.register("", PublicTestimonialViewSet, basename="testimonials")

urlpatterns = router.urls
