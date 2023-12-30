from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('class',views.classes,name='class'),
    path('team',views.team,name='team'),
    path('gallery',views.gallery,name='gallery'),
]