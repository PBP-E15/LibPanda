from django.shortcuts import render
from django.shortcuts import render, redirect
from wishlist.models import WishlistItem
from wishlist.models import Book
from django.contrib.auth.decorators import login_required
# Create your views here.
#@login_required
def show_wishlist(request):
    #wishlist_items = WishlistItem.objects.filter(user=request.user)
    wishlist_items = WishlistItem.objects.all
    context = {
        'wishlist_items': wishlist_items
    }

    return render(request, 'wishlist.html', context)

#@login_required
def add_wishlist(request, book_id):
    book = Book.objects.get(pk=book_id)

    # Membuat catatan dalam WishlistItem
    WishlistItem.objects.get_or_create(user=request.user, book=book)

    return redirect('wishlist')

#@login_required
def remove_wishlist(request, wishlist_item_id):
    wishlist_item = WishlistItem.objects.get(pk=wishlist_item_id)

    if wishlist_item.user == request.user:
        wishlist_item.delete()

    return redirect('wishlist')