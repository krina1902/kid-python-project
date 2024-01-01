from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('class',views.classes,name='class'),
    path('team',views.team,name='team'),
    path('gallery',views.gallery,name='gallery'),
    path('blogdetail',views.blogdetail,name='blogdetail'),
    path('bloggrid',views.bloggrid,name='bloggrid'),
    path('signup',views.signup,name='signup'),
]