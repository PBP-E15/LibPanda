from django.urls import path
from FormRequest.views import request_book
from main.views import login_user

app_name = 'request-book'

urlpatterns = [
    path('request-book/', request_book, name='request_book'),
]