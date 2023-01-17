from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, \
    DetailView
from .forms import FileCreateForm
from .models import File


class FilesListView(LoginRequiredMixin, ListView):
    login_url = 'authentication:signin_view'
    template_name = 'core/list_files.html'

    def get_queryset(self):
        return File.objects.all()


class AddFileView(LoginRequiredMixin, CreateView):
    form_class = FileCreateForm
    template_name = 'core/list_files.html'
    success_url = reverse_lazy('core:files_list_view')


class DetailFileView(LoginRequiredMixin, DetailView):
    pass


class UpdateFileView(LoginRequiredMixin, UpdateView):
    pass


class DeleteFileView(LoginRequiredMixin, DeleteView):
    model = File
    success_url = reverse_lazy('core:files_list_view')
