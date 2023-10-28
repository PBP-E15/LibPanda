from django.contrib import admin
from django.urls import include, path
from FormRequest.views import request_book
from main.views import login_user, logout_user, register, show_main


urlpatterns = [
    path('', show_main, name='show_main'),
    path('admin/', admin.site.urls),
    path("api/books", include("book.urls")),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),  
    path('request-book/', request_book, name='request_book'),
]