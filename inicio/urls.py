from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('acerca-de-mi/', views.acerca_de_mi_view, name='acerca_de_mi'),
]
