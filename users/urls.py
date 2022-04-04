from django.urls import path, include
from .views import register,  user_logout, user_login, profile, AboutView
from django.contrib.auth import views

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='user_logout'),
    path('login/', user_login, name='user_login'),
    path('profile/', profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
]
