from django.urls import path
from bookdetails.views import book_details

app_name = 'bookdetails'

urlpatterns = [

    path('details/<int:book_id>/', book_details, name='book_details'),

   
]

