from django.urls import path
from search_page.views import show_search_page,get_books_json,get_books_price_sorted_json

app_name = 'search_page'

urlpatterns = [
    path('search/', show_search_page, name='search'),
    path('get-books/', get_books_json, name='get_books_json'),
    path('get-books-price-sorted/',get_books_price_sorted_json, name='get_books_price_sorted_json')

]