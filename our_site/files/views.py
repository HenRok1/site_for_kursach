from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ResumeForm
from django.db.models import Q # новый

from .models import Resume
from django.views.generic import ListView


# Создайте здесь представления.

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/") 
    else:
        form = ResumeForm
    return render(request, 'files/upload.html', {'form':form})


class SearchResultsView(ListView):
    model = Resume
    template_name = 'files/search_result.html'
 
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Resume.objects.filter(
            Q(name__icontains=query) | Q(file__icontains=query)
        )
        return object_list