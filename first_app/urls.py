
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'), 
    path('login/', views.user_login, name='login'), 
    path('logout/', views.logout_view, name='logout'), 
    path('profile/', views.profile, name='profile'), 
    path('change_password/', views.pass_change, name='change_password'), 
    path('forgot_password/', views.set_password, name='forgot_password'), 

]
