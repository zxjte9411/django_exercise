from django.urls import path

from . import views

app_name = 'stores'

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store_list, name='store_list'),
    path('store/<pk>', views.store_detail, name='store_detail'),
]
