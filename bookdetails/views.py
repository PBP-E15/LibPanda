from django.shortcuts import render, get_object_or_404
from book.models import Book 
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    book.formatted_price = "Rp {:,.0f}".format(book.price)

    context = {
        'book': book,
        'name' : request.user.username,
        'user' : request.user,
    }

    return render(request, 'details.html', context)
