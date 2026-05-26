from rest_framework import serializers

from .models import NavItem


class NavItemSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = NavItem
        fields = ["id", "label", "url", "order", "parent", "children", "is_active", "open_in_new_tab"]

    def get_children(self, obj):
        children = obj.children.filter(is_active=True)
        return NavItemSerializer(children, many=True, context=self.context).data
