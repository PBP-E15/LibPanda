from django.urls import path
from FormRequest.views import request_book
from main.views import login_user

app_name = 'FormRequest'

urlpatterns = [
    path('request-book/', request_book, name='request-book'),
    path('accounts/login/', login_user, name='login_user'),
]