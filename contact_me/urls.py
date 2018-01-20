from django.urls import path
from . import views

app_name = 'contact_me'

urlpatterns = [
    path('', views.contact_me, name='contact_me'),
    path('email_success/', views.email_success, name='email_success'),
]