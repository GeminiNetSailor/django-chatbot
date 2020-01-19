from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', views.AuthUserHome.as_view(), name='auth-user-home'),
]
