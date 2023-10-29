from django.contrib import admin
from django.urls import path, include
from main.views import login_user, logout_user, register, show_main
from FormRequest.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'), 
    path('logout/', logout_user, name='logout'),
]