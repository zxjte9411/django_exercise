from django.shortcuts import render

from .models import Store


def home(request):
    return render(request, 'home.html')


def store_list(request):
    stores = Store.objects.all()
    return render(request, 'store_list.html', {'stores': stores})