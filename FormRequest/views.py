from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .forms import BookForm
from django.contrib.auth.decorators import login_required

@login_required
def request_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Periksa apakah ini adalah permintaan AJAX
                response = JsonResponse({'success': True})
            else:
                response = HttpResponse()
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False})
    else:
        form = BookForm()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Jika ini adalah permintaan AJAX, kirim respons kosong
        response = HttpResponse()
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'  # Menambahkan header Cache-Control
        return response

    return render(request, 'form.html', {'form': form})


