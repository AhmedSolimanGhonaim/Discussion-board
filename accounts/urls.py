from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from boards.views import home

urlpatterns  = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='accounts/change_password.html'), name='change_password'),
]
