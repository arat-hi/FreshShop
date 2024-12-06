from django.contrib import admin
from . import views
from django.urls import path
urlpatterns = [

path('',views.home),
    path('about',views.about),
    path('contact',views.contact),
    path('gallery',views.gallery),
    path('add',views.add , name='add'),

]
