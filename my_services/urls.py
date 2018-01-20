from django.urls import path
from . import views

app_name = 'my_services'

urlpatterns = [
    path('', views.my_services, name='my_services')
]