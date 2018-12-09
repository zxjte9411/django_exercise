from django.shortcuts import render

from django.views.generic import CreateView, DetailView
from .forms import EventForm
from .models import Event


class EventCreateView(CreateView):
    http_method_names = ['post']
    form_class = EventForm
    model = Event


class EventDetailView(DetailView):
    model = Event
