from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import MenuDocument, MenuPageImage
from .serializers import MenuDocumentSerializer, MenuPageImageSerializer


class PublicMenuDocumentViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = "slug"
    serializer_class = MenuDocumentSerializer

    def get_queryset(self):
        return MenuDocument.objects.filter(is_active=True).prefetch_related("pages")


class PublicMenuPageImageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MenuPageImageSerializer
    filterset_fields = ["document__slug"]

    def get_queryset(self):
        queryset = MenuPageImage.objects.filter(is_active=True, document__is_active=True).select_related("document")
        document = self.request.query_params.get("document")
        if document:
            queryset = queryset.filter(document__slug=document)
        return queryset


class AdminMenuDocumentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = MenuDocument.objects.all().prefetch_related("pages")
    serializer_class = MenuDocumentSerializer
    lookup_field = "slug"


class AdminMenuPageImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = MenuPageImage.objects.all().select_related("document")
    serializer_class = MenuPageImageSerializer


@api_view(["GET"])
def current_menu(request):
    document = (
        MenuDocument.objects.filter(is_active=True, is_default=True).prefetch_related("pages").first()
        or MenuDocument.objects.filter(is_active=True).prefetch_related("pages").first()
    )
    if not document:
        return Response(None)
    return Response(MenuDocumentSerializer(document, context={"request": request}).data)
