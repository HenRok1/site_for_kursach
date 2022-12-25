from django.urls import reverse_lazy

from .models import Kurs
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class KursCreate(CreateView):
    model = Kurs
    fields = '__all__'
    success_url = '/fillin/retrieves'


class KursRetrieve(ListView):
    model = Kurs
    success_url = reverse_lazy('kurs: KursRetrieve')


class KursDetail(DetailView):
    model = Kurs
    success_url = reverse_lazy('kurs: KursRetrieve')


class KursUpdate(UpdateView):
    model = Kurs
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = '/fillin/retrieves'

    # def get_success_url(self):


class KursDelete(DeleteView):
    model = Kurs
    # here we can specify the URL
    # to redirect after successful deletion
    success_url = '/fillin/retrieves'
