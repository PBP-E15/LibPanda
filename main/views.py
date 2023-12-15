from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from book.models import Book
from random import sample
from django.core import serializers


def show_main(request):
    books = Book.objects.all()
    
    shuffled_books = sample(list(books), len(books))

    for book in shuffled_books:
        book.formatted_price = "Rp {:,.0f}".format(book.price)

    context = {
        'books': shuffled_books,
        'name' : request.user.username,
        'user' : request.user
    }

    return render(request, "main.html", context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Autentikasi pengguna setelah mendaftar
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:show_main')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.delete_cookie('last_login')
    return response

def get_books_json(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books))