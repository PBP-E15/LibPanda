from django.urls import path
from shoppingcart.views import show_cart, add_bookcart, remove_bookcart, buy_book_ajax, show_json, add_cart_flutter, remove_cart_flutter, buy_cart_flutter

app_name = 'shoppingcart'

urlpatterns = [
    path('', show_cart, name='show_cart'),
    path('add_bookcart/<int:book_id>/', add_bookcart, name='add_bookcart'),
    path('remove_bookcart/<int:bookcart_id>/', remove_bookcart, name='remove_bookcart'),
    path('buy-book/<int:book_cart_id>/', buy_book_ajax, name='buy_book'),
    path('json/', show_json, name='show_json'),
    path('add_cart_flutter/', add_cart_flutter, name='add_cart_flutter'),
    path('remove_cart_flutter/', remove_cart_flutter, name='remove_cart_flutter'),
    path('buy_cart_flutter/', buy_cart_flutter, name='buy_cart_flutter'),
]