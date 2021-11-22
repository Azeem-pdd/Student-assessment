from django.contrib import admin
from django.urls import path, include
from .views import LoginView,LogoutView, RegisterView, IndexView
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]