from django.urls import path
from shoppingcart.views import show_cart, add_bookcart, delete_bookcart, buy_book_ajax, show_json

app_name = 'shoppingcart'

urlpatterns = [
    path('', show_cart, name='show_cart'),
    path('add_bookcart/<int:id>/', add_bookcart, name='add_bookcart'),
    path('delete_bookcart/<int:id>', delete_bookcart, name='delete_bookcart'),
    path('buy-book/<int:id>', buy_book_ajax, name='buy_book'),
    path('json/', show_json, name='show_json'),
]