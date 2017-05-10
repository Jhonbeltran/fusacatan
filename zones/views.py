from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import Zone
from .forms import ZoneForm

class ZoneCreate(LoginRequiredMixin, CreateView):
    model = Zone
    success_url = reverse_lazy('zones:zone')
    fields = ['date', 'location', 'moisture',
    	      'rainfall', 'trees']

class ZoneList(ListView):
    model = Zone

class ZoneDetail(LoginRequiredMixin, DetailView):
    model = Zone

class ZoneUpdate(LoginRequiredMixin, UpdateView):
    model = Zone
    success_url = reverse_lazy('zones:zone')
    fields = ['date', 'location', 'moisture',
    	      'rainfall', 'trees']


class ZoneDelete(LoginRequiredMixin, DeleteView):
    model = Zone
    success_url = reverse_lazy('zones:zone')
