from django.shortcuts import render
from book.models import Book
from random import sample

# Create your views here.
def show_main(request):
    # Get all books
    books = Book.objects.all()

    # Randomly shuffle the books
    shuffled_books = sample(list(books), len(books))

    for book in shuffled_books:
        book.formatted_price = "Rp {:,.0f}".format(book.price)

    context = {
        'books': shuffled_books
    }

    return render(request, "main.html", context)
