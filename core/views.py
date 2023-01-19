from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, \
    DetailView
from .forms import FileUploadForm
from .models import File


class FilesListView(LoginRequiredMixin, ListView):
    login_url = 'authentication:signin_view'
    template_name = 'core/list_files.html'

    def get_queryset(self):
        return File.objects.filter(owner=self.request.user)


class AddFileView(LoginRequiredMixin, CreateView):
    form_class = FileUploadForm
    template_name = 'core/add_file.html'
    success_url = reverse_lazy('core:files_list_view')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.owner = self.request.user
            file.save()

        return redirect(self.success_url)


class DetailFileView(LoginRequiredMixin, DetailView):
    template_name = ''

    def get_object(self, queryset=None):
        pass


class UpdateFileView(LoginRequiredMixin, UpdateView):
    model = File
    form_class = FileUploadForm
    template_name = 'core/update_file.html'
    success_url = reverse_lazy('core:files_list_view')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        if self.form_valid:
            self.object.status = File.UPDATED_STATUS
            self.object.save()

        return redirect(self.success_url)


class DeleteFileView(LoginRequiredMixin, DeleteView):
    model = File
    template_name = 'core/delete_file.html'
    success_url = reverse_lazy('core:files_list_view')
