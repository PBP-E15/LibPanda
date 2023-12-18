import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from shoppingcart.models import WalletUser, BookUser
from book.models import Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.urls import reverse


@login_required(login_url='/login')
def show_cart (request):
    totalHarga = 0
    books = BookUser.objects.filter(user=request.user)

    for book in books:
        totalHarga += book.book.price

    context = {
        'books' : books,
        'total' : totalHarga,
        'name' : request.user.username,
        'user' : request.user
    }

    return render(request, "cart.html", context)

@login_required(login_url='/login')
def add_bookcart(request, book_id):

    user = request.user
    book = Book.objects.get(pk=book_id)

    BookUser.objects.get_or_create(user=request.user, book=book)

    return HttpResponse(b"CREATED", status=201)

@login_required(login_url='/login')
@csrf_exempt
def remove_bookcart(request, bookcart_id):

    book = Book.objects.get(pk=bookcart_id)
    books = BookUser.objects.get(pk=bookcart_id)

    books.delete()

    return HttpResponse(b"DELETED", status=201)

@csrf_exempt
def buy_book_ajax(request, book_cart_id):
    totalHarga = 0
    wallet = WalletUser.objects.filter(user=request.user)
    books = BookUser.objects.filter(user=request.user)

    for book in books:
        totalHarga += book.price

    buku = BookUser.objects.get(pk = book_cart_id)

    if request.method == 'POST':
        buku.delete()
        wallet.balance -= totalHarga

        return HttpResponseRedirect(reverse('main:show_main'))
    return HttpResponseNotFound()

def show_json(request):
    user = request.user
    items = BookUser.objects.filter(user = user)
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

@login_required(login_url='/login')
@csrf_exempt
def add_cart_flutter(request):
    try:
        user = request.user
        data = json.loads(request.body)
        book_id = data.get('book_id')
        book = Book.objects.get(pk=book_id)

        if BookUser.objects.filter(user=user, book=book).exists():
            return JsonResponse({'status': 'Book is already in the shopping cart'}, status=400)

        BookUser.objects.create(user=user, book=book)

        return JsonResponse({'status': 'Book added to shopping cart successfully'}, status=201)

    except Exception as e:
        return JsonResponse({'status': 'Error adding book to shopping cart', 'error': str(e)}, status=500)

@login_required(login_url='/login')
@csrf_exempt
def remove_cart_flutter(request):
    try:
        user = request.user
        data = json.loads(request.body)
        book_id = data.get('book_id')
        book_item = BookUser.objects.get(user=user, id=book_id)
        book_item.delete()

        return JsonResponse({'status': 'Book removed from shopping cart successfully'}, status=201)

    except Exception as e:
        return JsonResponse({'status': 'Error adding book to shopping cart', 'error': str(e)}, status=500)