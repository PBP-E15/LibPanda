from django.shortcuts import render
from shoppingcart.models import WalletUser, BookUser
from book.models import Book
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import datetime
import json

@login_required(login_url='/login')
def show_cart (request):
    totalHarga = 0
    books = BookUser.objects.filter(user=request.user)

    for book in books:
        totalHarga += book.price

    context = {
        'books' : books,
        'total' : totalHarga,
        'name' : request.user.username,
        'user' : request.user
    }

    return render(request, "cart.html", context)

@login_required(login_url='/login')
def add_bookcart(request, id):

    user = request.user

    book = Book.objects.get(pk=id)

    BookUser.objects.get_or_create(user=request.user, book=book)

    return HttpResponse(b"CREATED", status=201)

def delete_bookcart(request, id):
    BookUser.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse('shoppingcart:cart'))

@csrf_exempt
def buy_book_ajax(request, id):
    totalHarga = 0
    wallet = WalletUser.objects.filter(user=request.user)
    books = BookUser.objects.filter(user=request.user)

    for book in books:
        totalHarga += book.price

    buku = BookUser.objects.get(pk = id)

    if request.method == 'POST':
        buku.delete()
        wallet.balance -= totalHarga

        return HttpResponseRedirect(reverse('main:show_main'))
    return HttpResponseNotFound()

def show_json(request):
    user = User.objects.get(user=request.user)
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