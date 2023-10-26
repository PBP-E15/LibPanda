from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# @login_required(login_url='/login') tunggu register page buat login
def delete_book(request, id):
    # Get data berdasarkan ID
    book = Product.objects.get(pk = id)
    # Hapus data
    book.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))