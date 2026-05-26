from rest_framework.routers import DefaultRouter

from .views import AdminTestimonialViewSet

router = DefaultRouter()
router.register("", AdminTestimonialViewSet, basename="admin-testimonials")

urlpatterns = router.urls
