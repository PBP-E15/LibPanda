from django.shortcuts import render, get_object_or_404
from book.models import Book 

def book_details(request, book_id):
    # Get the book with the specified book_id, or return a 404 error if not found
    book = get_object_or_404(Book, id=book_id)
    
    # Format the price
    book.formatted_price = "Rp {:,.0f}".format(book.price)

    context = {
        'book': book
    }

    return render(request, 'details.html', context)
