from django.urls import reverse_lazy

from .models import Liblinks
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class LiblinksCreate(CreateView):
    model = Liblinks
    fields = '__all__'
    success_url = '/liblinks/retrieves'


class LiblinksRetrieve(ListView):
    model = Liblinks
    success_url = reverse_lazy('Liblinks: LiblinksRetrieve')


class LiblinksDetail(DetailView):
    model = Liblinks
    success_url = reverse_lazy('Liblinks: LiblinksRetrieve')


class LiblinksUpdate(UpdateView):
    model = Liblinks
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = '/liblinks/retrieves'

    # def get_success_url(self):


class LiblinksDelete(DeleteView):
    model = Liblinks
    # here we can specify the URL
    # to redirect after successful deletion
    success_url = '/liblinks/retrieves'
