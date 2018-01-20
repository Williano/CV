from django.urls import path
from . import views

app_name = 'my_education'

urlpatterns = [
    path('', views.my_education, name='my_education')
]