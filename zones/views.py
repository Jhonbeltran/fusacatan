from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import Zone
from .forms import EventForm

class EventCreate(LoginRequiredMixin, CreateView):
    model = Zone
    success_url = reverse_lazy('zones:zone')
    fields = ['date', 'location', 'moisture',
    	      'rainfall', 'trees']

class EventList(ListView):
    model = Zone

class EventDetail(LoginRequiredMixin, DetailView):
    model = Zone

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Zone
    success_url = reverse_lazy('zones:zone')
    fields = ['date', 'location', 'moisture',
    	      'rainfall', 'trees']


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Zone
    success_url = reverse_lazy('zones:zone')
