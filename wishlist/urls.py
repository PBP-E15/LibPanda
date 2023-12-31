from django.urls import path
from wishlist.views import add_wishlist_flutter, removed_wishlist_flutter, show_wishlist, remove_wishlist, add_wishlist,show_json, check_wishlist

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='wishlist'),
    path('remove_wishlist/<int:wishlist_item_id>/', remove_wishlist, name='remove_wishlist'),
    path('add_wishlist/<int:book_id>/', add_wishlist, name='add_wishlist'),
    path('json/', show_json, name='show_json'),
    path('wishlist/check_wishlist/<int:book_id>/', check_wishlist, name='check_wishlist'),
    path('add_wishlist_flutter/', add_wishlist_flutter, name='add_wishlist_flutter'),
    path('removed_wishlist_flutter/', removed_wishlist_flutter, name='removed_wishlist_flutter'),
    
]