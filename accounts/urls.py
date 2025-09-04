from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('cart/', views.cart_view, name='cart'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('change-password/', views.change_password_view, name='change_password'),
]