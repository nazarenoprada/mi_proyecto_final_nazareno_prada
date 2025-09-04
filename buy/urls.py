from django.urls import path
from . import views

app_name = 'buy'

urlpatterns = [
    path('', views.buy_view, name='buy'),
    path('finish/', views.finish_buy_view, name='finish_buy'),
]
