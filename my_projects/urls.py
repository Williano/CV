from django.urls import path
from . import views

app_name = 'my_projects'

urlpatterns = [
    path('', views.my_projects, name='my_projects')
]