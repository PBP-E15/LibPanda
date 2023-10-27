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
from user_profile.models import Biodata, Wallet

# @login_required(login_url='/login')
def show_profile(request):
    try:
        biodata = Biodata.objects.filter(user=request.user)
        wallet = Wallet.objects.filter(user=request.user)

        context = {
            'name': request.user.username,
            'biodata' : biodata,
            'wallet' : wallet,
        }
    except:


        context = {
    
        }

    return render(request, "profile.html", context)

def edit_biodata(request, id):
    if request.method == 'POST':
        biodata = Biodata.objects.get(pk=id)
    
        biodata.name = request.POST.get("name")
        biodata.email = request.POST.get("email")
        biodata.gender = request.POST.get("gender")
        biodata.birthday = request.POST.get("description")

        response = HttpResponse(status=200)
        return response
    return HttpResponseNotFound()

def topup_wallet(request, id):
    if request.method == 'POST':
        wallet = Wallet.objects.get(pk=id)

        wallet.balance += request.POST.get("topup")

        response = HttpResponse(status=200)
        return response
    return HttpResponseNotFound()

def get_biodata_json(request):
    biodata_item = Biodata.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', biodata_item))

def get_wallet_json(request):
    wallet_item = Wallet.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', wallet_item))

# Create your views here.
