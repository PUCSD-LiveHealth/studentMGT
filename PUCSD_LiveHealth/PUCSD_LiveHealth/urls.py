"""PUCSD_LiveHealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  from rest_framework.urlpatterns import format_suffix_patterns
from empApp import viewsurl(r'^blog/', include('blog.urls'))
"""
from rest_framework.urlpatterns import format_suffix_patterns
from studentMgt import views
from django.conf.urls import url 
from django.contrib import admin
from studentMgt.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', renderlogin),
    url(r'^dashboard/', login),
    url(r'^logout/', logout),
    url(r'^foo/', foo),
    url(r'^sessionValues/',sessionValues),
    url(r'^insertparent/',createParent), 
    url(r'^insertstudent/',createStudent),


]
