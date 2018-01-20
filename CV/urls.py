"""CV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('about_me/', include('about_me.urls', namespace='about_me')),
    path('contact_me/', include('contact_me.urls', namespace='contact_me')),
    path('experience/', include('experience.urls', namespace='experience')),
    path('my_education/', include('my_education.urls', namespace='my_education')),
    path('my_projects/', include('my_projects.urls', namespace='my_projects')),
    path('my_services/', include('my_services.urls', namespace='my_services')),
    path('my_skills/', include('my_skills.urls', namespace='my_skills')),
    path('admin/', admin.site.urls),
]
