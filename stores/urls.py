from django.urls import path

from . import views 

app_name = 'stores'

urlpatterns = [
    path('', views.home, name='home'),
]