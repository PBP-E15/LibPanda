from django.shortcuts import render
from .models import Book
from main.views import *
#from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


# Create your views here.
#@login_required
def form_request(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        category = request.POST.get('category')
        synopsis = request.POST.get('synopsis')
        year = request.POST.get('year')
        new_request = Book(title=title, author=author, category=category, synopsis=synopsis, year=year)
        new_request.save()
        return render(request, 'success.html') #tbd
    return render(request, 'form.html') #tbd

def data(request):
    all_requests = Book.objects.all()
    return render(request, 'data.html', {'requests': all_requests})

def delete(request, item_id):
    book = get_object_or_404(Book, pk=item_id, user=request.user)
    book.delete()
    return render(request, 'data.html')