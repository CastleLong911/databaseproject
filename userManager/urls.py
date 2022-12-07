from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import userManager
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('signup_form/', views.signup_form, name='signup_form'),
    path('ajax_username_check/', views.ajax_username_check, name='ajax_username_check'),

]