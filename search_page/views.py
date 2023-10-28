from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from book.models import Book

def show_search_page(request):
    books = Book.objects.all()

    context = {
        'books': books,
        'name' : request.user.username,
        'user' : request.user,
    }

    return render(request, "search.html", context)

def get_books_json(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books))

def get_books_price_sorted_json(request):
    books = list(Book.objects.all())

    for step in range(1, len(books)):
        key = books[step]
        j = step - 1

        while j >= 0 and key.price < books[j].price:
            books[j + 1] = books[j]
            j = j - 1

        books[j + 1] = key

    return HttpResponse(serializers.serialize('json', books))


