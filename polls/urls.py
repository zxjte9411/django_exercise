from django.urls import path

from . import views

urlpatterns = [
    path('hellowWorld/', views.hellowWorld, name='hellowWorld'),
    path('', views.index, name='index'),
]