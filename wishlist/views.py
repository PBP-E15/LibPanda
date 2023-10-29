import json
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from wishlist.models import WishlistItem
from book.models import Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

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
    user = User.objects.get(pk=1)
    #user = request.user
    book = Book.objects.get(pk=book_id)
    # Membuat catatan dalam WishlistItem
    WishlistItem.objects.get_or_create(user=user, book=book)
    #WishlistItem.objects.get_or_create(user=request.user, book=book)

    return HttpResponse(b"CREATED", status=201)

#@login_required
@csrf_exempt
def remove_wishlist(request, wishlist_item_id):
    user = User.objects.get(pk=1)
    #user = request.user
    book = Book.objects.get(pk=wishlist_item_id)
    wishlist_item = WishlistItem.objects.get(pk=wishlist_item_id)

    #if wishlist_item.user == request.user:
    wishlist_item.delete()

    return HttpResponse(b"DELETED", status=201)

def show_json(request):
    user = User.objects.get(pk = 1) # Nanti ganti jadi request.user
    items = WishlistItem.objects.filter(user = user)
    serialized_data = []
    for item in items:

        model_data = {
            "pk" : item.pk,
            "book": {
                "thumbnail" : item.book.thumbnail,
                "title" : item.book.title,
                "authors" : item.book.authors,
                "average_rating" : item.book.average_rating,
                "price" : item.book.price,
                "categories" : item.book.categories
            }
        }
        serialized_data.append(model_data)

    json_data = json.dumps(serialized_data)
    return HttpResponse(json_data, content_type="application/json")

