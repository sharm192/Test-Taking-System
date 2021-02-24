"""TestTakingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
import SchoolManagement.views as SMViews

urlpatterns = [
    path('admin/', admin.site.urls),
    # Homepage inside the School Management System 
    path('', SMViews.home),
    # URL for login
    url(r'^login/$', SMViews.login, name='login'),
    url(r'^profile/$', SMViews.profile, name='profile'),
    path('faceid/', SMViews.faceid.as_view(), name ='faceid')    
]
