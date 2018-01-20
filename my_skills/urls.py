from django.urls import path
from . import views

app_name = 'my_skills'

urlpatterns = [
    path('', views.my_skills, name='my_skills')
]