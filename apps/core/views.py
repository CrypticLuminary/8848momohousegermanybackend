from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(["GET"])
def health_check(request):
    return Response({"status": "ok"})


class DashboardSummaryView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        from apps.blogs.models import BlogPost
        from apps.cms.models import Page, PageSection
        from apps.franchise.models import FranchiseInquiry
        from apps.gallery.models import GalleryImage
        from apps.menu.models import MenuPageImage
        from apps.navigation.models import NavItem
        from apps.reservations.models import Reservation
        from apps.settings_app.models import SiteSettings

        def label_for(obj):
            for attr in ("title", "name", "caption", "label", "question", "site_name"):
                value = getattr(obj, attr, "")
                if value:
                    return value
            if isinstance(obj, PageSection):
                return f"{obj.page.title}: {obj.section_key}"
            if isinstance(obj, MenuPageImage):
                return obj.title or f"{obj.document.title} page {obj.order}"
            return str(obj)

        def changed_at_for(obj):
            return getattr(obj, "updated_at", None) or getattr(obj, "submitted_at", None) or getattr(obj, "created_at", None)

        activity_sources = [
            ("Menu", MenuPageImage.objects.select_related("document").all()),
            ("Blogs", BlogPost.objects.all()),
            ("Gallery", GalleryImage.objects.all()),
            ("Reservations", Reservation.objects.all()),
            ("Pages", Page.objects.all()),
            ("Sections", PageSection.objects.select_related("page").all()),
            ("Navigation", NavItem.objects.all()),
            ("Franchise inquiries", FranchiseInquiry.objects.all()),
            ("Settings", SiteSettings.objects.all()),
        ]

        activity = []
        for area, queryset in activity_sources:
            items = sorted(queryset[:200], key=lambda obj: changed_at_for(obj), reverse=True)[:8]
            for obj in items:
                changed_at = changed_at_for(obj)
                created_at = getattr(obj, "created_at", None) or getattr(obj, "submitted_at", None)
                action = "Created" if created_at == changed_at else "Updated"
                activity.append(
                    {
                        "title": f"{action} {label_for(obj)}",
                        "area": area,
                        "action": action,
                        "at": changed_at.isoformat(),
                    }
                )
        activity = sorted(activity, key=lambda item: item["at"], reverse=True)[:20]
        last_updated = activity[0]["at"] if activity else None

        stats = {
            "menuItems": MenuPageImage.objects.count(),
            "blogs": BlogPost.objects.count(),
            "reservations": Reservation.objects.count(),
            "inquiries": FranchiseInquiry.objects.count(),
            "galleryImages": GalleryImage.objects.count(),
            "pages": Page.objects.count(),
            "sections": PageSection.objects.count(),
            "navigationItems": NavItem.objects.count(),
            "lastUpdated": last_updated or "No activity",
        }
        return Response({"stats": stats, "activity": activity})
