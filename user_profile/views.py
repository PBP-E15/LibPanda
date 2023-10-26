from django.shortcuts import render
from user_profile.models import Biodata, Wallet

def show_profile(request):
    context = {
        'name': 'LOL',
        'class': 'PBP E'
    }

    return render(request, "profile.html", context)
# Create your views here.
