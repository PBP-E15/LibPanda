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

@login_required(login_url='/login')
def show_wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    context = {
        'wishlist_items': wishlist_items,
        'name' : request.user.username,
        'user' : request.user,
    }

    return render(request, 'wishlist.html', context)

@login_required(login_url='/login')
def add_wishlist(request, book_id):
    user = request.user
    book = Book.objects.get(pk=book_id)
    WishlistItem.objects.get_or_create(user=request.user, book=book)

    return HttpResponse(b"CREATED", status=201)

@login_required(login_url='/login')
@csrf_exempt
def remove_wishlist(request, wishlist_item_id):
    book = Book.objects.get(pk=wishlist_item_id)
    wishlist_item = WishlistItem.objects.get(pk=wishlist_item_id)

    wishlist_item.delete()

    return HttpResponse(b"DELETED", status=201)

def show_json(request):
    user = request.user
    items = WishlistItem.objects.filter(user = user)
    serialized_data = []
    for item in items:
        in_wishlist = True

        model_data = {
            "pk" : item.pk,
            "book": {
                "thumbnail" : item.book.thumbnail,
                "title" : item.book.title,
                "authors" : item.book.authors,
                "average_rating" : item.book.average_rating,
                "price" : item.book.price,
                "categories" : item.book.categories,
                "in_wishlist": in_wishlist,
            }
        }
        serialized_data.append(model_data)

    json_data = json.dumps(serialized_data)
    return HttpResponse(json_data, content_type="application/json")

def check_wishlist(request, book_id):
    user = request.user 
    try:
        wishlist_item = WishlistItem.objects.get(user=user, book__pk=book_id)
        in_wishlist = True
    except WishlistItem.DoesNotExist:
        in_wishlist = False

    response_data = {'inWishlist': in_wishlist}
    return HttpResponse(json.dumps(response_data), content_type='application/json')