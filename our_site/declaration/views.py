from django.urls import reverse_lazy

from .models import Declaration
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class DeclarationCreate(CreateView):
    model = Declaration
    fields = '__all__'
    success_url = '/declare/retrieves'


class DeclarationRetrieve(ListView):
    model = Declaration
    success_url = reverse_lazy('Declaration: KursRetrieve')


class DeclarationDetail(DetailView):
    model = Declaration
    success_url = reverse_lazy('Declaration: KursRetrieve')


class DeclarationUpdate(UpdateView):
    model = Declaration
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = '/declare/retrieves'

    # def get_success_url(self):


class DeclarationDelete(DeleteView):
    model = Declaration
    # here we can specify the URL
    # to redirect after successful deletion
    success_url = '/declare/retrieves'
