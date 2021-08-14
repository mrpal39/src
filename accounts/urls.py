from django.shortcuts import render
from django.urls.conf import path
from . views import *





urlpatterns =[

    path('',home_page, name='homepage')



]