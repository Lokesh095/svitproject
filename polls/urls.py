from django.urls import path

from . import views

urlpatterns = [
    path('test', views.hello, name='index1' ),
    path('aboutus', views.index, name='index'),
    
]