from django.contrib import admin
from django.urls import path, include
from main.views import login_user, logout_user, register, show_main
from FormRequest.views import *

urlpatterns = [
    path('', show_main, name='show_main'),
    #path('accounts/login/', login_user, name='login'), 
]