from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('m-data',views.m_data,name='mdata'),
    path('stazioni_appaltanti',views.stazioni_appaltanti)
]
