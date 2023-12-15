from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_profile.models import Biodata, Wallet

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    
    try:
        biodata = Biodata.objects.get(user=request.user)
        wallet = Wallet.objects.get(user=request.user)
    
    except:
        name = "fulan"
        email = "example@gmail.com"
        gender = ""
        birthday = "2004-05-04"
        phone_number = "040504"
        biodata = Biodata(user=user, name=name, email=email, gender=gender, birthday=birthday, phone_number=phone_number)
        biodata.save()
        
        balance = 0
        wallet = Wallet(user=user, balance=balance)
        wallet.save()
        
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "password": request.POST['password'],
                "wallet_pk": biodata.id,
                "biodata_pk": wallet.id,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)
