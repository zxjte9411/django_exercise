from django.urls import path

from . import views

app_name = 'events'


urlpatterns = [
    path('new/', views.EventCreateView.as_view(), name='event_create'),
    path('<int:pk>', views.EventDetailView.as_view(),
         name='event_detail'),
]
