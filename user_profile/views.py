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
from django.http import JsonResponse
import json
from user_profile.models import Biodata, Wallet

@login_required(login_url='/login')
def show_profile(request):
    try:
        user = request.user
        
        biodata = user.biodata
        wallet = user.wallet

        context = {
            'name': request.user.username,
            'biodata' : biodata,
            'wallet' : wallet,
        }
        
    except:
        user = request.user

        name = user.username
        email = "no_email@email.com"
        gender = ""
        birthday = "2004-05-04"
        phone_number = "040504"

        new_biodata = Biodata(user=user, name=name, email=email, gender=gender, birthday=birthday, phone_number=phone_number)
        new_biodata.save()

        balance = 0
        new_wallet = Wallet(user=user, balance=balance)
        new_wallet.save()

        context = {
            'name': request.user.username,
            'biodata' : new_biodata,
            'wallet' : new_wallet,
        }

    return render(request, "profile.html", context)

@csrf_exempt
def edit_biodata(request, id):
    if request.method == 'POST':
        biodata = Biodata.objects.get(pk=id)
    
        biodata.name = request.POST.get("name")
        biodata.email = request.POST.get("email")
        biodata.gender = request.POST.get("gender")
        biodata.birthday = request.POST.get("birthday")
        biodata.phone_number = request.POST.get("phone_number")
        biodata.save()

        response = HttpResponse(status=200)
        return response
    return HttpResponseNotFound()

@csrf_exempt
def topup_wallet(request, id):
    if request.method == 'POST':
        wallet = Wallet.objects.get(pk=id)
        wallet.balance += int(request.POST.get("balance"))
        wallet.save()

        response = HttpResponse(status=200)
        return response
    return HttpResponseNotFound()

def get_biodata_json(request):
    biodata_item = Biodata.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', biodata_item))

def get_wallet_json(request):
    wallet_item = Wallet.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', wallet_item))

@csrf_exempt
def get_biodata_flutter(request, id):
    biodata_item = Biodata.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', biodata_item))

@csrf_exempt
def get_wallet_flutter(request, id):
    wallet_item = Wallet.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', wallet_item))

@csrf_exempt
def edit_biodata_flutter(request, id):
    if request.method == 'POST':

        biodata=Biodata.objects.get(pk=id)
        data = json.loads(request.body)

        biodata.name = data["name"]
        biodata.email = data["email"]
        biodata.gender = data["gender"]
        biodata.birthday = data["birthday"]
        biodata.phone_number = data["phone_number"]
        biodata.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def topup_wallet_flutter(request, id):
    if request.method == 'POST':

        wallet=Wallet.objects.get(pk=id)
        data = json.loads(request.body)

        wallet.balance += int(data["balance"])
        wallet.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)# Create your views here.
