from django.urls import path

from .views import DashboardSummaryView, health_check

urlpatterns = [
    path("health/", health_check, name="health-check"),
    path("dashboard/", DashboardSummaryView.as_view(), name="dashboard-summary"),
]
