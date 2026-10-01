from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Report
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'home.html')


class ReportCreateView(CreateView):
    form_class = ReportForm
    template_name = 'lost_found/report_form.html'
    success_url = reverse_lazy('report-list')


class ReportListView(ListView):
    model = Report
    context_object_name = 'reports'
    template_name = 'lost_found/reports.html'


class ReportDetailView(DetailView):
    model = Report
    pk_url_kwarg = 'id'
    context_object_name = 'report'
    template_name = 'lost_found/report_detail.html'


class ReportUpdateView(UpdateView):
    model = Report
    pk_url_kwarg = 'id'
    context_object_name = 'report'
    form_class = ReportForm
    template_name = 'lost_found/report_update.html'
    success_url = reverse_lazy('report-list')


class ReportDeleteView(DeleteView):
    model = Report
    pk_url_kwarg = 'id'
    context_object_name = 'report'
    success_url = reverse_lazy('report-list')
    template_name = 'lost_found/report_delete_confirmation.html'
