from django.urls import path
from .views import ReportCreateView, ReportListView, ReportDetailView, ReportUpdateView, ReportDeleteView


urlpatterns = [
    path('add-report/', ReportCreateView.as_view(), name='report-create'),
    path('reports/', ReportListView.as_view(), name='report-list'),
    path('report-detail/<int:id>/', ReportDetailView.as_view(), name='report-detail'),
    path('report-update/<int:id>/', ReportUpdateView.as_view(), name='report-update'),
    path('report/<int:id>/delete/', ReportDeleteView.as_view(), name='report-delete'),
]
