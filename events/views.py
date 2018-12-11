from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.views.generic import CreateView, DetailView
from .forms import EventForm, OrderForm
from .models import Event
from django.contrib.auth.mixins import LoginRequiredMixin


class EventCreateView(LoginRequiredMixin, CreateView):
    http_method_names = ['post']
    form_class = EventForm
    model = Event


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        order_form = OrderForm()
        order_form.fields['item'].queryset = self.object.store.menu_items.all()
        data['order_form'] = order_form
        return data

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest()
        # 產生 object（但先不要存進資料庫）
        order = form.save(commit=False)
        order.user = request.user
        order.event = self.get_object()
        order.save()
        return redirect(order.event.get_absolute_url())
